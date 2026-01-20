#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ai_running_milk_yogurt.py

1. 從 normalized_soda_updated.json 取示範，提供給 LLM 當格式範例。
2. 對 filtered_tea_coffe_milktea.json 依「品牌 → 系列/口味 → 容量」三層聚類。
3. 聚類結果直接寫回 rec["norm"]，並輸出 normalized_tea_coffe_milktea.json，
   依 norm 升序排序方便檢查（終端也僅列印唯一 norm）。
"""

import os
import json
import re
from collections import OrderedDict
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# ------------------ 工具 ----------------------------------------------------

CAP_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:ml|mL|ML|l|L|g|G)")

def _dedupe_keep_order(seq):
    seen = set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            yield x

def _clean_capacity(text: str) -> str:
    m = CAP_RE.search(text)
    if not m:
        return ""
    num = m.group(1)
    unit = "ml" if "l" not in m.group(0).lower() else "l"
    if unit == "l":
        num = str(int(float(num) * 1000))          # 1.5L → 1500ml
    return f"{num}ml"

def _clean_canonical(raw: str) -> str:
    parts = [p.strip() for p in raw.strip().split("→") if p.strip()]
    cleaned = " → ".join(_dedupe_keep_order(parts))
    if cleaned:
        pcs = cleaned.split(" → ")
        cap = _clean_capacity(pcs[-1])
        if cap:
            pcs[-1] = cap
        cleaned = " → ".join(pcs)
    return cleaned.lower()


# ------------------ 主流程 ---------------------------------------------------

def main() -> None:
    base = os.path.dirname(os.path.abspath(__file__))

    # 1) 讀示範（soda）
    demo_path = os.path.join(base, "normalized_soda_updated.json")
    with open(demo_path, encoding="utf-8") as f:
        soda = json.load(f)

    demo_clusters = OrderedDict()
    for rec in soda:
        demo_clusters.setdefault(rec["norm"], []).append(rec["norm"])

    example_blocks = [
        json.dumps({"canonical": canon, "members": sorted(set(mems))},
                   ensure_ascii=False, indent=2)
        for canon, mems in list(demo_clusters.items())[:10]   # 範例抓前 10 群
    ]
    demo_examples = "\n\n".join(example_blocks)

    # 2) 讀待處理檔
    src = os.path.join(base, "filtered_tea_coffe_milktea.json")
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    if not data:
        raise ValueError("filtered_tea_coffe_milktea.json 為空！")

    field = "norm" if "norm" in data[0] else "eng"
    names = list(_dedupe_keep_order(item.get(field, "") for item in data))
    print(f"⚙️ 使用欄位「{field}」聚類；樣本 {len(names)} 筆")

   # 3) LLM prompt ----------------------------------------------------------
    system_prompt = (
        "你是一个聚类助手，只返回纯 JSON，不要输出任何多余文字。\n"
        "请按照以下优先级，对【即饮茶／咖啡／奶茶】产品进行分层聚类：\n"
        "1. 品牌（如 asahi、nescafe、vita）\n"
        "2. 产品系列或口味（如 wonda、cold brew、lemon tea、无糖）\n"
        "3. 容量（统一写成数字+ml，例如 330ml、500ml、1500ml）\n"
        "为每个簇指定一个“规范名称”（canonical），格式如下：\n"
        "{\n"
        "  \"1\": {\"canonical\": \"品牌 → 系列/口味 → 容量\", \"members\": [\"…\", \"…\"]},\n"
        "  …\n"
        "}\n"
        "规则：\n"
        "• canonical 与 members 全部用小写，去掉多余空格、括号与包装说明。\n"
        "• 若无法判定品牌，用 \"unknown\" 代替。\n"
        "• 仅返回 JSON，不包含任何思考或说明。\n"
        "• 在思考部分和 JSON 部分之间，用一行 “----JSON----” 分隔。\n"
        "• 总簇数不得超过 ⌈样本数 ÷ 8⌉。\n"
    )
    # -----------------------------------------------------------------------

    api_url = "http://192.168.50.98:1234/v1/chat/completions"
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "產品清單如下：\n" + "\n".join(names)}
        ],
        "temperature": 0.0,
        "max_tokens": 12508
    }

    sess = requests.Session()
    sess.mount("http://", HTTPAdapter(
        max_retries=Retry(total=3, backoff_factor=1,
                          status_forcelist=[502, 503, 504],
                          allowed_methods=["POST"])
    ))

    try:
        res = sess.post(api_url, json=payload)
        res.raise_for_status()
    except Exception as exc:
        raise RuntimeError(f"🚨 呼叫本地 LLM 失敗：{exc}")

    content = res.json()["choices"][0]["message"]["content"]
    json_part = content.split("----JSON----", 1)[-1].strip()

    # 擷取最外層 JSON
    depth = 0; s = e = None
    for i, ch in enumerate(json_part):
        if ch == "{":
            if depth == 0:
                s = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                e = i
                break
    if s is None or e is None:
        raise ValueError("⚠️ 無法定位 JSON 區塊")
    clusters = json.loads(json_part[s:e+1])

    # 4) 清洗 canonical（相容兩種格式） ----------------------------- ###
    cleaned = OrderedDict()
    for outer_key, info in clusters.items():

        # ▶ ① 若 value 為 dict 且含 canonical
        if isinstance(info, dict) and "canonical" in info:
            canon_raw = info["canonical"]
            members_raw = info.get("members", [])
        # ▶ ② 否則把外層 key 當 canonical，value 應為 members list
        else:
            canon_raw = outer_key
            members_raw = info if isinstance(info, list) else []

        canon = _clean_canonical(canon_raw)
        members = sorted({m.lower() for m in members_raw})
        cleaned[canon] = {"canonical": canon, "members": members}
    # -------------------------------------------------------------- ###

    # 5) 建對照 & 回寫 norm
    name2canon = {}
    for info in cleaned.values():
        for m in info["members"]:
            key = re.sub(r"\s*\([^)]*\)", "", m).strip()
            name2canon[key] = info["canonical"]

    normalized = []
    for rec in data:
        raw = rec.get(field, "")
        key = re.sub(r"\s*\([^)]*\)", "", raw.lower()).strip()
        rec["norm"] = name2canon.get(key, key)       # 直接覆寫 norm
        normalized.append(rec)

    normalized.sort(key=lambda x: x["norm"])

    print("\n🔍 唯一 norm（供人工檢查）:")
    for n in OrderedDict.fromkeys(r["norm"] for r in normalized):
        print(" -", n)

    out = os.path.join(base, "normalized_tea_coffe_milktea.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)
    print(f"\n✅ 完成！{len(normalized)} 筆寫入 {out}")


if __name__ == "__main__":
    main()