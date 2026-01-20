#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def build_uid_name_map(products_data):
    """
    根据产品信息文件构建 uid 到产品名称（name）的映射字典
    """
    mapping = {}
    products = products_data.get("products_with_embeddings", [])
    for prod in products:
        uid = prod.get("uid", "").strip()
        name = prod.get("name", "").strip()  # 可根据需要使用其他字段（例如 core_name）也可替换
        if uid:
            mapping[uid] = name
    return mapping

def transform_clusters(clusters_data, uid_name_map):
    """
    遍历聚类结果，将每个聚类内的 uid 替换为对应产品名称
    如果找不到对应名称，则保留 uid（或标记为 "<unknown>"）
    """
    transformed_clusters = {}
    clusters = clusters_data.get("clusters", {})
    for cluster_id, uid_list in clusters.items():
        transformed_list = []
        for uid in uid_list:
            product_name = uid_name_map.get(uid, f"<unknown: {uid}>")
            transformed_list.append({"uid": uid, "name": product_name})
        transformed_clusters[cluster_id] = transformed_list
    return transformed_clusters

def main():
    # 使用绝对路径指定输入与输出文件
    clustering_result_file = "/Users/gary/Documents/Supermarket1/Json_data/clustering_result.json"
    products_file = "/Users/gary/Documents/Supermarket1/Json_data/products_with_bilingual_embeddings.json"
    output_file = "/Users/gary/Documents/Supermarket1/Json_data/clusters_with_names.json"

    print(f"[INFO] 加载聚类结果文件：{clustering_result_file}")
    clusters_data = load_json(clustering_result_file)

    print(f"[INFO] 加载产品信息文件：{products_file}")
    products_data = load_json(products_file)

    # 构建 UID 到产品名称的映射
    uid_name_map = build_uid_name_map(products_data)
    print(f"[INFO] 共有 {len(uid_name_map)} 条产品信息用于映射。")

    # 转换聚类结果：用名称替代 uid 信息
    transformed_clusters = transform_clusters(clusters_data, uid_name_map)

    # 构造输出结果
    output_data = {
        "update_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "clusters": transformed_clusters
    }

    # 保存输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    print(f"[INFO] 转换完成，结果已保存到：{output_file}")

if __name__ == "__main__":
    main()