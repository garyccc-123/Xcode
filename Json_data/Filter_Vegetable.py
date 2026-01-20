
import json
import re
import logging

# —— 配置區 ——
INPUT_FILES = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]
OUTPUT_FILE = '/Users/gary/Documents/Supermarket1/Json_data/filtered_vegetable.json'

# 常見要移除的包裝詞（簡寫＋全寫＋新增g/pcs）
REMOVE_TERMS = [
    'gm','gram','grams',
    'ea','each',
    'pc','pcs','piece','pieces',
    'lb','pound',
    'pk','pack',
    'bx','box',
    'cs','case',
    'g'
]


def normalize_name(name):
    """
    依指示進行歸一化處理
    """
    s = name.lower()
    # 去括號及其中內容
    s = re.sub(r'\(.*?\)', ' ', s)
    # 去數字
    s = re.sub(r'\d+', ' ', s)
    # 移除包裝詞
    for t in REMOVE_TERMS:
        s = re.sub(r'\b' + re.escape(t) + r'\b', ' ', s)
    # 只保留字母和空格
    s = re.sub(r'[^a-z\s]', ' ', s)
    # 壓縮多餘空格
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def load_products():
    """
    讀入兩檔，提取蔬菜類商品
    """
    items = []
    for path in INPUT_FILES:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for p in data.get('products', []):
            # 只保留 sub_categories 中包含 '蔬菜' 的項目
            if '蔬菜' not in p.get('sub_categories', []):
                continue
            uid = p.get('uid')
            eng = p.get('product_eng_name', '').strip()
            if uid and eng:
                items.append({'uid': uid, 'eng': eng})
    logging.info(f'載入蔬菜原始紀錄：{len(items)} 條')
    return items


def dedupe(items, key):
    """
    依指定 key（uid or eng）去重
    """
    seen = set()
    out = []
    for it in items:
        val = it[key]
        if val in seen:
            continue
        seen.add(val)
        out.append(it)
    return out


def main():
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    # 1) 讀取 PNS / Wellcome 兩檔資料
    items = load_products()

    # 2) 依 UID 去重
    before = len(items)
    items = dedupe(items, 'uid')
    logging.info(f'去重 UID 後剩餘：{len(items)} 條 (原 {before} 條)')

    # 3) 依英文名去重
    before = len(items)
    items = dedupe(items, 'eng')
    logging.info(f'去重英文名後剩餘：{len(items)} 條 (原 {before} 條)')

    # 4) 歸一化
    for it in items:
        it['norm'] = normalize_name(it['eng'])

    # 5) 寫出 JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    logging.info(f'已寫入：{OUTPUT_FILE}')


if __name__ == '__main__':
    main()
