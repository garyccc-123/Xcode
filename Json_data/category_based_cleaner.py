#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
腳本名稱：category_based_cleaner.py
描述：
  從包含多家超市數據的 JSON 文件中（例如 "all_data_for_clean.json"），
  提取每個產品的信息（保留 "core_name", "product_eng_name", "uid" 以及 "sub_categories"），
  並按照產品的第一個 sub_categories（若不存在或為空，則歸到 "Uncategorized"）分組。
  每個 subcategory 的分組資料會分別保存成一個 JSON 文件，文件名中保留中文。
  
  注意：請根據實際情況修改輸入和輸出資料夾的絕對路徑。
"""

import json
import os
import datetime
import re

def load_products(input_path):
    """
    加載包含多家超市數據的 JSON 文件，遍歷所有以 "_store" 結尾的頂層鍵，
    將其中 "products" 數組中的每個產品增加一個 "store" 字段。
    返回所有產品的列表。
    """
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    products = []
    for key, store_data in data.items():
        if key.endswith("_store"):
            for prod in store_data.get("products", []):
                if prod is None:
                    continue
                prod["store"] = key
                products.append(prod)
    return products

def group_products_by_subcategory(products):
    """
    根據每個產品的 sub_categories（取列表的第一項，如果不存在或空白則歸為 "Uncategorized"）
    對產品進行分組。每個產品僅保留 uid、name、product_eng_name 及 store（去除首尾空格）。
    
    返回格式：
      {
         "<sub_category1>": [ { "uid": ..., "name": ..., "product_eng_name": ..., "store": ... }, ... ],
         "<sub_category2>": [ ... ],
         ...
      }
    """
    groups = {}
    for prod in products:
        uid = (prod.get("uid") or "").strip()
        name = (prod.get("name") or "").strip()
        product_eng_name = (prod.get("product_eng_name") or "").strip()
        store = (prod.get("store") or "").strip()
        sub_cats = prod.get("sub_categories")
        if isinstance(sub_cats, list) and len(sub_cats) > 0 and sub_cats[0].strip():
            subcategory = sub_cats[0].strip()
        else:
            subcategory = "Uncategorized"

        clean_prod = {
            "uid": uid,
            "name": name,
            "product_eng_name": product_eng_name,
            "store": store
        }
        groups.setdefault(subcategory, []).append(clean_prod)
    return groups

def sanitize_filename(s):
    """
    將字串轉為適合用於文件名的格式：
      - 允許英文、數字、底線、破折號以及 CJK 統一表意符（中文字符範圍 \u4e00-\u9fff）
    如果 s 為空則返回 "Uncategorized"。
    """
    s = s.strip()
    if not s:
        s = "Uncategorized"
    return re.sub(r'[^\w\-\u4e00-\u9fff]+', '_', s)

def save_subcategory_json(output_dir, subcategory, products):
    """
    將某個 subcategory 下的產品資料保存成一個 JSON 文件。
    文件名格式：<sub_category_cleaned>_cleaned.json
    """
    update_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    out_data = {
        "update_date": update_date,
        "subcategory": subcategory,
        "products": products
    }
    filename = sanitize_filename(subcategory) + "_cleaned.json"
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, "w", encoding="utf-8") as f_out:
        json.dump(out_data, f_out, ensure_ascii=False, indent=4)
    print(f"[INFO] {subcategory} 分组数据保存到：{output_path}")

def main():
    # 修改下面的輸入文件和輸出資料夾的絕對路徑
    input_file = "/Users/gary/Documents/Supermarket1/Json_data/all_data_for_clean.json"
    output_dir = "/Users/gary/Documents/Supermarket1/Json_data/subcategory_clusters"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"[INFO] 正在加载文件：{input_file}")
    products = load_products(input_file)
    print(f"[INFO] 加载到 {len(products)} 条产品数据。")
    
    grouped = group_products_by_subcategory(products)
    print(f"[INFO] 分组完成，共生成 {len(grouped)} 个 subcategory 分组。")
    
    # 分別保存每個 subcategory 的數據
    for subcategory, prod_list in grouped.items():
        save_subcategory_json(output_dir, subcategory, prod_list)
    
    print("[INFO] 所有数据保存完毕。")

if __name__ == "__main__":
    main()