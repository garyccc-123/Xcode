#!/usr/bin/env python3
# vegetable_ai_running.py

import os
import json
import re
import requests


def main():
    # 1️⃣ 定位 JSON 文件
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filtered_path = os.path.join(BASE_DIR, 'filtered_vegetable.json')
    with open(filtered_path, encoding='utf-8') as f:
        data = json.load(f)
    if not data:
        raise ValueError("filtered_vegetable.json 为空！")

    # 2️⃣ 选用聚类字段：优先使用 norm，否则使用 eng
    field = 'norm' if 'norm' in data[0] else 'eng'
    print(f"⚙️ 使用字段“{field}”进行蔬菜聚类。")

    # 3️⃣ 构造 Prompt 列表
    names = sorted({item.get(field, '') for item in data})
    vegetable_list = "\n".join(names)

    # 4️⃣ 发送请求到本地 LM Studio（Deepseek）
    API_URL = "http://192.168.50.98:1234/v1/chat/completions"  # 替换为你的 IP:端口
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": (
                "你是一个聚类助手，只返回纯 JSON，不要输出任何多余文字。\n"
                "在分组时请遵循以下规则：\n"
                "1. 忽略所有品牌、产地、包装或重量信息（如 ‘MR VEGETABLE’、‘(pack)’、‘200g’ 等），"
                "示例：‘MR VEGETABLE Spring Onions’ → ‘spring onion’，‘CAMERON HIGHLANDS carrot’ → ‘carrot’。\n"
                "2. 只保留核心蔬菜品类名称，使用单数形式（如 ‘pepper’ 而非 ‘peppers’）。\n"
                "3. 将同一品类的颜色、尺寸或包装变体合并到同一个簇"
                "（如 ‘red pepper’、‘green pepper’ 均归为 ‘pepper’；‘baby asparagus’、‘green asparagus’ 均归为 ‘asparagus’）。\n"
                "4. 对于 ‘fresh herbs’ 系列，分别命名 thyme、rosemary、parsley、basil、mint，"
                "示例：‘CAMERON HIGHLANDS Fresh Herbs Thyme’ → ‘thyme’。\n"
                "5. 严格返回如下 JSON 结构：\n"
                "{\n"
                "  \"1\": {\"canonical\": \"规范名称\", \"members\": [\"成员1\", \"成员2\", …]},\n"
                "  \"2\": {…}\n"
                "}\n"
                "6. 请在思考部分和 JSON 部分之间，用一行 “----JSON----” 分隔：\n"
                "   — 分隔符前是你的思考；\n"
                "   — 分隔符后立即开始输出纯 JSON，并确保最外层大括号完整匹配。"
            )},
            {"role": "user", "content": (
                "下面是一组蔬菜名称列表，请按照上述规则进行聚类并输出。\n"
                "蔬菜列表：\n" + vegetable_list
            )}
        ],
        "temperature": 0.0,
        "max_tokens": 12508
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()

    # 5️⃣ 拆分思考与 JSON
    content = response.json()["choices"][0]["message"]["content"]
    parts = content.split("----JSON----", 1)
    think_part, json_part = (parts + ["", ""])[:2]

    # 写入思考到 debug.txt
    debug_path = os.path.join(BASE_DIR, "debug.txt")
    with open(debug_path, "w", encoding="utf-8") as dbg:
        dbg.write(think_part.strip())
    print(f"📝 已将模型思考写入：{debug_path}")

    # 5.1️⃣ 用深度计数截取最外层 JSON
    text = json_part.strip()
    depth = 0
    start_idx = None
    end_idx = None
    for i, ch in enumerate(text):
        if ch == '{':
            depth += 1
            if start_idx is None:
                start_idx = i
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end_idx = i
                break
    if start_idx is None or end_idx is None:
        # 如果定位失败，可以在这里打印 json_part 方便调试
        print("----JSON PART----")
        print(json_part)
        raise ValueError("无法定位最外层 JSON 的起止位置。")
    json_text = text[start_idx:end_idx+1]

    # 5.2️⃣ 解析 JSON 部分
    try:
        clusters = json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 解析失败：{e}\nJSON 内容：\n{json_text}")

    # 6️⃣ 合并原始数据并添加 canonical_name
    fix_map = {
        # Herbs & 简单替换
        "cameron highlands fresh herbs thyme":    "thyme",
        "cameron highlands fresh herbs rosemary": "rosemary",
        "cameron highlands fresh herbs parsley":  "parsley",
        "cameron highlands fresh herbs basil":    "basil",
        "cameron highlands fresh herbs mint":     "mint",

        # mr vegetable 前缀
        "mr vegetable spring onions":             "spring onion",
        "mr vegetable potato":                    "potato",
        "mr vegetable choi sum":                  "choi sum",
        "mr vegetable coriander":                 "coriander",

        # “pak choi” 相关
        "three zero baby pak choi":                "pak choi",
        "three zero baby pak choy":                "pak choi",
        "cameron highlands hydroponic small pak choi": "pak choi",

        # “choy sum” 统一为 “choi sum”
        "three zero choy sum":                     "choi sum",
        "choy sum":                                "choi sum",

        # 统一拼写 / 复数 -> 单数
        "spring onions":          "spring onion",
        "tomatoes":               "tomato",
        "cherry tomatoes":        "tomato",
        "red cherry tomatoes":    "tomato",
        "orange cherry tomatoes": "tomato",
        "romantic mini plum tomatoes": "tomato",
        "passion mini cherry tomatoes": "tomato",
        "magical tomatoes on the vine":  "tomato",
        "cherry tomatoes on the vine":   "tomato",
        "new zealand beekist angel tomato": "tomato",

        "shallots":     "shallot",
        "sugar snaps":  "sugar snap beans",

        # 包装/产地前缀
        "prepack tomato":           "tomato",
        "prepacked tomato":         "tomato",
        "prepacked small choi sum": "choi sum",
        "prepack carrot":           "carrot",

        "usa baby carrot":         "carrot",
        "red carrot":              "carrot",
        "australia carrot snackables": "carrot",

        "usa baking potatoes":     "potato",
        "new potatoes":            "potato",
        "farmfresh new potatoes":  "potato",
        "prepacked potato":        "potato",

        # 洋葱
        "brown onion": "onion",
        "red onion":   "onion",
        "onion kg":    "onion",
        "onion red":   "onion",

        # 生菜
        "iceburg lettuce":            "iceberg lettuce",
        "aqua green romaine lettuce": "lettuce",

        # 蘑菇类
        "farmfresh crimini":               "crimini",
        "kgmp king oyster mushroom":       "king oyster mushroom",
        "korean oyster king mushroom":     "king oyster mushroom",
        "hokio white honshimeij mushroom": "mushroom",
        "hokio taiwan honshimeiji mushroom":"mushroom",
        "kgmp enoki mushroom":             "enoki mushroom",

        # 其它
        "lemon grass":           "lemongrass",
        "courettes zucchini":    "zucchini",
        "h k brown button mushroom": "mushroom",
        "h k white button mushroom": "mushroom",
        "organic portabella mushroom": "portabella mushroom",
        "organic portobello mushroom":  "portobello mushroom",

        # 新增的项
        "a vegetable sprout":            "bean sprout",
        "buddhism melon":                "melon",
        "jade melon":                    "melon",
        "aqua green butter green hydro": "lettuce",
        "aqua green oakleaf green hydro":"lettuce",
        "meadows korean enoki mushroom":"enoki mushroom",
        "import snow peas":              "snow peas",
        "pak choy sprouts":              "pak choi sprouts",
        "australia broccolini":          "broccolini",
        "broccolini":                    "broccolini",
        "broccoli":                      "broccolini",
        "cameron highlands hydroponic pumpkin":"pumpkin",
        "cameron highlands hydroponic salad mix":"salad mix",
        "mixed hotpot set":              "hotpot set",
        "butter green hydro":             "lettuce",
        "oakleaf green hydro":            "lettuce",
        "organic soya bean sprout":            "sprout",
        "red tomato":            "tomato",
        "kenya sugar snap beans":            "snow bean",
        "beans":            "snow bean",
        "import sugar snaps":            "snow bean",
        "green asparagus":            "asparagus",
        "cilembu honey sweet potato":            "sweet potato",
        "sweet bean":            "snow bean",
        
        # 空值
        "": "",
    }

    # 构建 name->canonical 的映射
    name2canon = {
        nm: info.get("canonical", nm)
        for info in clusters.values()
        for nm in info.get("members", [])
    }

    normalized = []
    seen_canons = set()
    for item in data:
        raw = item.get(field, "")
        # 1️⃣ 归一化为小写并去掉括号及其内容
        norm = raw.lower()
        norm = re.sub(r'\s*\([^)]*\)', '', norm)

        # 2️⃣ 一次性去除所有常见品牌/产地/包装/hydroponic/hydro 前缀
        norm = re.sub(
            r'^(?:mr vegetable|meadows|import|farmfresh|redstar|grace cup|'
            r'cameron highlands(?: fresh herbs?)?|fresh herbs?|'
            r'hydroponic(?:s)?|hydro)\s+',
            '',
            norm,
            flags=re.IGNORECASE
        )

        # 3️⃣ 批量去掉 "mr vegetable " 前缀（多余保险）
        if norm.startswith("mr vegetable "):
            norm = norm[len("mr vegetable "):]
        if norm.startswith("hydroponic "):
            norm = norm[len("hydroponic "):]

        # 4️⃣ 优先用 fix_map
        if norm in fix_map:
            canon = fix_map[norm]
        else:
            # 5️⃣ 否则用聚类结果
            canon = name2canon.get(norm, norm)

        item['canonical_name'] = canon
        normalized.append(item)
        seen_canons.add(canon)

    # 打印所有 unique canonical_name，便于复核
    print("🔍 所有 unique canonical_name 值：")
    for c in sorted(seen_canons):
        print(f"- {c}")

    # 7️⃣ 输出结果
    output_path = os.path.join(BASE_DIR, 'normalized_vegetable.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)
    print(f"✅ 已生成 {output_path}，共 {len(normalized)} 条记录。")

def __main__():
    main()

if __name__ == "__main__":
    main()
