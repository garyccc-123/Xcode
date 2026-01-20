#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
從 filtered_plant_milk.json 讀取植物奶名稱，呼叫本地 LLM 依
「品牌 → 系列/風味 → 容量」三層聚類，並對 canonical 進一步清洗、排序；
最後把結果寫回 normalized_plant_milk.json，並依 canonical_name 升序排序。
"""
import os
import json
import re
from collections import OrderedDict
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---------- 小工具 --------------------------------------------------


def _dedupe_keep_order(seq):
    """保持順序去重"""
    seen = set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            yield x


_CAP_PAT = re.compile(r"(\d+(?:\.\d+)?)\s*(?:ml|mL|ML|l|L)")

def _clean_capacity(text: str) -> str:
    """把容量統一轉成數字+ml（全部小寫、無空格）"""
    m = _CAP_PAT.search(text)
    if not m:
        return ""
    num = m.group(1)
    unit = "l" if "l" in m.group(0).lower() and "ml" not in m.group(0).lower() else "ml"
    if unit == "l":
        num = str(int(float(num) * 1000))
    return f"{num}ml"


def _clean_canonical(raw: str) -> str:
    """移除多餘箭頭、空白，容量統一"""
    parts = [p.strip() for p in raw.strip().split("→") if p.strip()]
    cleaned = " → ".join(_dedupe_keep_order(parts))
    if cleaned:
        items = cleaned.split(" → ")
        items[-1] = _clean_capacity(items[-1]) or items[-1]
        cleaned = " → ".join(items)
    return cleaned.lower()


# ---------- 主流程 --------------------------------------------------


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. 讀檔
    src_path = os.path.join(base_dir, "filtered_plant_milk.json")
    with open(src_path, encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        raise ValueError("filtered_plant_milk.json 內無資料！")

    # 2. 選欄位
    field = "norm" if "norm" in data[0] else "eng"
    print(f"⚙️ 使用欄位「{field}」進行聚類。")

    # 3. 建 prompt（保留原始順序去重）
    names = list(_dedupe_keep_order(item.get(field, "") for item in data))
    item_list = "\n".join(names)

    # 4. 呼叫本地 LLM
    api_url = "http://192.168.50.98:1234/v1/chat/completions"
    system_prompt = """
你是「植物奶名稱聚類助手」。
# 目標
把下列【豆奶 / 燕麥奶 / 杏仁奶 …】名稱依「品牌 → 系列/風味 → 容量」三層聚類，僅輸出 JSON。
# 規則
1. **品牌**：取英文（或拼音）裡的品牌，如 VITASOY, OATLY, BLUE DIAMOND。
2. **系列/風味**：剝掉容量與包裝描述，保留共同子品牌或口味：如 calci plus、barista、unsweetened、chocolate。
3. **容量**：擷取數值+單位（統一 ml，小寫，無空格，如 1000ml）。
4. 缺少品牌資訊時品牌填 "unknown"。
5. **輸出要求**
   • canonical 不能與任何 members 完全相同。
   • members 與 canonical 都要小寫；各自字典序排序。
   • 總簇數 ≤ ⌈(輸入條目數)/8⌉；單簇 members ≤ 50。
6. 僅回傳 JSON，格式示例：
{
  "1": {"canonical": "vitasoy → calci plus → 250ml", "members": ["vitasoy calci plus hi-calcium oat soya drink 250ml", ...]},
  "2": {"canonical": "oatly → barista → 1000ml", "members": ["oatly barista oat drink 1lt", ...]}
}
在思考內容與 JSON 之間，用一行 ----JSON---- 分隔。
""".strip()

    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"以下為產品清單，請依規則聚類並回傳純 JSON：\n{item_list}"}
        ],
        "temperature": 0.0,
        "max_tokens": 15000
    }

    sess = requests.Session()
    sess.mount("http://", HTTPAdapter(max_retries=Retry(total=3,
                                                       backoff_factor=1,
                                                       status_forcelist=[502, 503, 504],
                                                       allowed_methods=["POST"])))
    try:
        r = sess.post(api_url, json=payload)
        r.raise_for_status()
    except Exception as exc:
        raise RuntimeError(f"呼叫本地 LLM 失敗：{exc}")

    content = r.json()["choices"][0]["message"]["content"]

    # 5. 取出 JSON 片段
    json_block = content.split("----JSON----", 1)[-1].strip()
    depth = start = end = 0
    for i, ch in enumerate(json_block):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
    if depth != 0:
        raise ValueError("無法擷取 LLM 回傳的最外層 JSON。")

    clusters = json.loads(json_block[start:end + 1])

    # 6. 清洗 canonical + 重新排序
    cleaned = OrderedDict()
    for key, info in sorted(clusters.items(), key=lambda kv: _clean_canonical(kv[1]["canonical"])):
        canonical = _clean_canonical(info["canonical"])
        members = sorted({m.lower() for m in info.get("members", [])})
        cleaned[key] = {"canonical": canonical, "members": members}

    # 7. 建 name→canonical 對照
    name2canon = {}
    for info in cleaned.values():
        canon = info["canonical"]
        for m in info["members"]:
            norm_m = re.sub(r"\s*\([^)]*\)", "", m).strip()
            name2canon[norm_m] = canon

    # 8. 寫回原資料並依 canonical_name 排序
    normalized = []
    for item in data:
        raw = item.get(field, "")
        key = re.sub(r"\s*\([^)]*\)", "", raw.lower()).strip()
        item["canonical_name"] = name2canon.get(key, key)
        normalized.append(item)

    normalized.sort(key=lambda x: x["canonical_name"])

    # 9. 輸出
    out_path = os.path.join(base_dir, "normalized_plant_milk.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)

    print(f"✅ 已產生 {out_path}，共 {len(normalized)} 筆。")


if __name__ == "__main__":
    main()