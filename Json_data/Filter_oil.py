import json
import logging
import re
from pathlib import Path

# —— 配置区 ——
INPUT_FILES = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]
OUTPUT_FILE = '/Users/gary/Documents/Supermarket1/Json_data/filtered_oil.json'

def load_products():
    """
    读取两个 JSON，筛出「油」子分类的记录，仅保留 uid / eng 字段
    """
    items = []
    for path in INPUT_FILES:
        if not Path(path).exists():
            logging.warning(f"⚠️ 找不到檔案: {path}")
            continue
            
        logging.info(f"正在讀取: {path}")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                wrapper = json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"❌ JSON 格式錯誤 {path}: {e}")
            continue

        # 1. 兼容不同的根目錄結構
        if isinstance(wrapper, list):
            products_list = wrapper
        elif isinstance(wrapper, dict):
            products_list = wrapper.get('products', [])
        else:
            logging.warning(f"⚠️ 未知的資料結構: {type(wrapper)}")
            continue

        for p in products_list:
            # 2. 🛡️ 安全檢查：確保 p 是字典
            if not isinstance(p, dict):
                continue

            # ❗️子分类里必须有 “油”
            # 使用 safe get 避免報錯
            sub_cats = p.get('sub_categories', [])
            if not isinstance(sub_cats, list): # 確保 sub_categories 也是 list
                continue
                
            if '油' not in sub_cats:
                continue
                
            uid = p.get('uid')
            eng = (p.get('product_eng_name') or '').strip()

            if uid and eng:
                items.append({'uid': uid, 'eng': eng})

    logging.info(f'载入油原始记录：{len(items)} 条')
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
    if not isinstance(txt, str): return ""
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