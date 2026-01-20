#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import logging

# 请根据实际情况修改这几个路径
UNKNOWN_UIDS_PATH = '/Users/gary/Documents/Supermarket1/Json_data/unknown_brands.json'
INPUT_FILES = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]
OUTPUT_PATH = '/Users/gary/Documents/Supermarket1/Json_data/unknown_products_full.json'

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def load_unknown_uids(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # 如果是 dict，则扁平化所有 value 列表
    if isinstance(data, dict):
        uids = []
        for subcat, lst in data.items():
            if isinstance(lst, list):
                uids.extend(lst)
        return uids
    # 如果本来就是 list，直接返回
    elif isinstance(data, list):
        return data
    else:
        logging.error("unknown_brands.json 格式不支持，必须是 list 或 dict")
        return []

def load_all_products(paths):
    all_prods = {}
    total = 0
    for p in paths:
        with open(p, 'r', encoding='utf-8') as f:
            js = json.load(f)
        prods = js.get('products', []) or js.get('products_clean', [])
        logging.info(f"从 {os.path.basename(p)} 加载 {len(prods)} 条商品")
        for item in prods:
            uid = item.get('uid')
            if uid:
                all_prods[uid] = item
        total += len(prods)
    logging.info(f"合并后共索引 {len(all_prods)} 条唯一商品 (原始载入 {total} 条)")
    return all_prods

def main():
    # 1. 读取并扁平化 UNKNOWN UID 列表
    unknown_uids = load_unknown_uids(UNKNOWN_UIDS_PATH)
    logging.info(f"加载到 {len(unknown_uids)} 个 UNKNOWN UID")

    # 2. 读取所有商品，按 uid 建索引
    prod_index = load_all_products(INPUT_FILES)

    # 3. 匹配 UNKNOWN UID，收集详情
    matched = {}
    not_found = []
    for uid in unknown_uids:
        prod = prod_index.get(uid)
        if prod:
            matched[uid] = prod
        else:
            not_found.append(uid)

    logging.info(f"成功匹配 {len(matched)} 条 UNKNOWN 商品")
    if not_found:
        logging.warning(f"以下 {len(not_found)} 个 UID 未找到：{not_found[:10]}{'...' if len(not_found)>10 else ''}")

    # 4. 输出完整详情
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump({
            "matched_count": len(matched),
            "not_found_count": len(not_found),
            "matched_products": list(matched.values()),
            "not_found_uids": not_found
        }, f, ensure_ascii=False, indent=2)
    logging.info(f"已将 UNKNOWN 商品详情写入：{OUTPUT_PATH}")

if __name__ == '__main__':
    main()