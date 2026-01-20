#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
import itertools
import random
import argparse
from collections import defaultdict

# 常量配置
BRAND_DICT_PATH = '/Users/gary/Documents/Supermarket1/json_data/brand_dict_fixed.json'
INPUT_FILES     = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]
OUTPUT_PAIRS    = '/Users/gary/Documents/Supermarket1/Json_data/pairs.json'
UNKNOWN_OUTPUT  = '/Users/gary/Documents/Supermarket1/Json_data/unknown_brands.json'

def load_brand_dict(path):
    """
    递归扁平化任意层级的品牌字典 JSON，
    最终返回 subcat -> [ (en, zh), ... ]
    支持 list 或 dict 顶层。
    """
    raw = json.load(open(path, 'r', encoding='utf-8'))
    flat = {}

    def process_entry(key, val):
        # 如果值是列表，就把每个元素当「这一 subcat 的品牌」来处理
        if isinstance(val, list):
            pairs = []
            for b in val:
                if isinstance(b, dict) and 'en' in b and 'zh' in b:
                    pairs.append((b['en'], b['zh']))
                elif isinstance(b, str):
                    if '（' in b and b.endswith('）'):
                        en = b.split('（',1)[0].strip()
                        zh = b.split('（',1)[1][:-1].strip()
                    else:
                        en = zh = b
                    pairs.append((en, zh))
            if pairs:
                flat[key] = pairs

        # 如果值是 dict，继续下钻
        elif isinstance(val, dict):
            for k2, v2 in val.items():
                process_entry(k2, v2)

    # 支持顶层 list 或 dict
    if isinstance(raw, list):
        for part in raw:
            if isinstance(part, dict):
                for k, v in part.items():
                    process_entry(k, v)
    elif isinstance(raw, dict):
        for k, v in raw.items():
            process_entry(k, v)

    return flat

def load_products(files):
    """
    遍历两个超市的 JSON 文件，提取 (uid, subcategory, eng)，
    并按 uid + eng_name 两层去重，返回去重后展开到各子類別的项列表。
    """
    seen_uids = set()
    seen_names = set()
    items = []
    raw_count = 0

    for path in files:
        data = json.load(open(path, 'r', encoding='utf-8'))
        prods = data.get('products', [])
        raw_count += len(prods)
        for p in prods:
            uid = p.get('uid')
            eng = p.get('product_eng_name', '').strip().lower()
            if not uid or not eng:
                continue
            # 双重去重：uid 或 英文名 重复都跳过
            if uid in seen_uids or eng in seen_names:
                continue
            seen_uids.add(uid)
            seen_names.add(eng)
            for sub in p.get('sub_categories', []):
                items.append({'uid': uid, 'subcategory': sub, 'eng': eng})

    logging.info(f"載入原始記錄：{raw_count} 條，"
                 f"唯一商品（去重后）：{len(seen_uids)} 條，"
                 f"展開 UID×子類 组合后：{len(items)} 條")
    return items

def assign_brand(item, brand_list):
    """
    简单的 brand 打标：若英文或中文品牌名出现在产品英文名中，即归为该品牌。
    """
    name = item['eng']
    for en, zh in brand_list:
        if en.lower() in name or zh.lower() in name:
            return en
    return 'UNKNOWN'

def group_by_subcat_brand(items, brand_map):
    """
    按 subcategory 和 brand 分组，返回 grouped[subcat][brand] = [uid,...]
    """
    grouped = defaultdict(lambda: defaultdict(list))
    for it in items:
        lst = brand_map.get(it['subcategory'], [])
        b = assign_brand(it, lst)
        grouped[it['subcategory']][b].append(it['uid'])
    return grouped

def generate_pairs(grouped, neg_ratio=1.0, seed=42):
    """
    根据 grouped 生成正负样本对：
    正样本 label=1，同 subcat 同 brand
    负样本 label=0，同 subcat 不同 brand，个数 = 正样本数 * neg_ratio
    """
    random.seed(seed)
    pairs = []
    for sub, brands in grouped.items():
        # 正样本
        pos = []
        for brand, uids in brands.items():
            for a, b in itertools.combinations(uids, 2):
                pos.append({'uid_a': a, 'uid_b': b, 'label': 1})
        pairs.extend(pos)

        # 负样本
        all_brands = [b for b, us in brands.items() if us]
        neg = []
        num_neg = int(len(pos) * neg_ratio)
        if len(all_brands) >= 2:
            for _ in range(num_neg):
                b1, b2 = random.sample(all_brands, 2)
                a  = random.choice(brands[b1])
                bb = random.choice(brands[b2])
                neg.append({'uid_a': a, 'uid_b': bb, 'label': 0})
        pairs.extend(neg)

        logging.info(f"子類別「{sub}」：正 {len(pos)}，負 {len(neg)}")
    total_pos = sum(1 for p in pairs if p['label']==1)
    total_neg = sum(1 for p in pairs if p['label']==0)
    logging.info(f"總對數：{len(pairs)} (正 {total_pos}, 負 {total_neg})")
    return pairs

def main():
    parser = argparse.ArgumentParser(description="生成商品 pair-wise 訓練集")
    parser.add_argument('-s','--subcat', help="只生成此子類別的 pair-wise（默認全部）")
    parser.add_argument('--neg-ratio', type=float, default=1.0, help="負樣本與正樣本比例")
    parser.add_argument('--seed',      type=int,   default=42,  help="隨機種子")
    parser.add_argument('--log-level', choices=['DEBUG','INFO','WARNING','ERROR'], default='INFO')
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging,args.log_level),
                        format='[%(levelname)s] %(message)s')

    brand_map = load_brand_dict(BRAND_DICT_PATH)
    items     = load_products(INPUT_FILES)

    # 可選按子類別篩選
    if args.subcat:
        before = len(items)
        items = [it for it in items if it['subcategory'] == args.subcat]
        logging.info(f"已篩選子類別「{args.subcat}」，"
                     f"從 {before} 條剩 {len(items)} 條")

    grouped = group_by_subcat_brand(items, brand_map)

    # 輸出 UNKNOWN
    unknown = {sub: uids for sub, bs in grouped.items() if (uids := bs.get('UNKNOWN'))}
    if unknown:
        with open(UNKNOWN_OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(unknown, f, ensure_ascii=False, indent=2)
        logging.warning(f"發現 UNKNOWN，共 {sum(len(v) for v in unknown.values())} 筆，已寫入 {UNKNOWN_OUTPUT}")

    # 生成並輸出 pairs
    pairs = generate_pairs(grouped, neg_ratio=args.neg_ratio, seed=args.seed)
    with open(OUTPUT_PAIRS, 'w', encoding='utf-8') as f:
        json.dump(pairs, f, ensure_ascii=False, indent=2)
    logging.info(f"已輸出 pair-wise 檔案：{OUTPUT_PAIRS}")

if __name__ == '__main__':
    main()