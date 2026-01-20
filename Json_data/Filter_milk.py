import json
import logging
import re
from pathlib import Path

# —— 配置区 ——
INPUT_FILES = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]
OUTPUT_FILE = '/Users/gary/Documents/Supermarket1/Json_data/filtered_milk.json'

def load_products():
    """
    读取两个 JSON，筛出「奶類、乳酪飲品」子分类的记录，仅保留 uid / eng 字段
    """
    items = []
    for path in INPUT_FILES:
        with open(path, 'r', encoding='utf-8') as f:
            wrapper = json.load(f)

        for p in wrapper.get('products', []):
            # ❗️子分类里必须有 “奶類、乳酪飲品”
            if '奶類、乳酪飲品' not in p.get('sub_categories', []):
                continue
            uid = p.get('uid')
            eng = (p.get('product_eng_name') or '').strip()

            if uid and eng:
                items.append({'uid': uid, 'eng': eng})

    logging.info(f'载入奶類、乳酪飲品原始记录：{len(items)} 条')
    return items

def dedupe(items, key):
    """
    根据 key 去重，保留第一次出现的条目
    """
    seen = set()
    out = []
    for it in items:
        v = it[key]
        if v in seen:
            continue
        seen.add(v)
        out.append(it)
    return out

def clean_backslash(txt: str) -> str:
    r"""
    将 “非法 / 多余” 的反斜杠做最小化清洗，避免 json.dumps 之后再被解析时报错
    - 转义残骸 \"  \'  -> 去掉反斜杠
    - 孤立反斜杠 \x   -> 删掉反斜杠
    （**只对 eng 字段做；uid 不动**）
    """
    # 1) 先处理 \" 和 \'
    txt = txt.replace(r'\"', '"').replace(r"\'", "'")
    # 2) 再把剩余孤立的 \ 变空
    txt = re.sub(r"\\(?![\\u\"'bfnrt])", '', txt)
    return txt

def main():
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    # 1️⃣ 读取
    items = load_products()

    # 2️⃣ 按 uid 去重
    before = len(items)
    items = dedupe(items, 'uid')
    logging.info(f'去重 UID 后剩余：{len(items)} 条 (原 {before} 条)')

    # 3️⃣ 轻量清洗反斜杠
    for it in items:
        it['eng'] = clean_backslash(it['eng'])

    # 4️⃣ 写出
    out_path = Path(OUTPUT_FILE)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    logging.info(f'✅ 已写入：{out_path} （共 {len(items)} 条记录）')

if __name__ == '__main__':
    main()
