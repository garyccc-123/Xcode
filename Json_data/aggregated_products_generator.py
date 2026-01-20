import json
import math
import os
import shutil
import logging
import time
from datetime import datetime
from rapidfuzz import process, fuzz

# ===== 配置参数 =====
CONFIG = {
    "input_file": "/Users/gary/Documents/Supermarket1/Json_data/all_data_clean_minimal.json",
    "output_file": "/Users/gary/Documents/Supermarket1/Json_data/aggregated_products.json",
    "backup": True,                     # 是否备份旧文件
    "backup_dir": "/Users/gary/Documents/Supermarket1/Json_data/backup",
    "similarity_threshold": 80,         # 相似度阈值，根据实际情况调整，可尝试80左右
    "progress_log_percent": 5           # 每处理百分之多少输出一次进度
}

# ===== 配置日志 =====
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def backup_file(file_path, backup_dir):
    """
    如果 file_path 存在，则将其备份到 backup_dir 中，
    备份文件名附加当前时间戳，方便版本追踪。
    """
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        base_name = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_name = f"{base_name}.{timestamp}.bak"
        backup_path = os.path.join(backup_dir, backup_name)
        shutil.copy2(file_path, backup_path)
        logging.info(f"备份成功：{file_path} -> {backup_path}")
    except Exception as e:
        logging.error(f"备份失败：{e}")

# ===== 并查集实现 =====
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def cluster_products_union_find(products, threshold):
    """
    利用 rapidfuzz.process.cdist 计算所有产品（依据 core_name）的相似度矩阵，
    并采用并查集算法将相似度大于等于 threshold 的产品归为同一组。
    过程中的进度每处理 progress_log_percent 的百分比输出一次。
    """
    # 提取每个产品的 core_name 作为聚类依据
    names = [p.get("core_name", "") for p in products]
    total = len(names)
    if total == 0:
        return []
    
    logging.info(f"计算 {total} 条产品 core_name 的相似度矩阵...")
    start_time = time.time()
    try:
        similarity_matrix = process.cdist(names, names, scorer=fuzz.ratio)
    except Exception as e:
        logging.error(f"相似度矩阵计算失败: {e}")
        return []
    elapsed = time.time() - start_time
    logging.info(f"相似度矩阵计算完成，耗时 {elapsed:.1f} 秒")
    
    uf = UnionFind(total)
    for i in range(total):
        for j in range(i + 1, total):
            try:
                if similarity_matrix[i][j] >= threshold:
                    uf.union(i, j)
            except Exception as e:
                logging.error(f"比较产品 {i} 与 {j} 时出错: {e}")
    
    # 构造聚类结果
    clusters_dict = {}
    for i in range(total):
        root = uf.find(i)
        clusters_dict.setdefault(root, []).append(products[i])
    
    # 输出分群进度（这里采用简单的计数方式，便于调试）
    log_interval = max(1, math.floor(total * (CONFIG.get("progress_log_percent") / 100)))
    clustering_start = time.time()
    for idx in range(total):
        if (idx + 1) % log_interval == 0 or (idx + 1) == total:
            progress = (idx + 1) / total * 100
            elapsed_cluster = time.time() - clustering_start
            logging.info(f"分群进度: {progress:.1f}% ({idx + 1}/{total})，耗时 {elapsed_cluster:.1f} 秒")
    
    clusters = list(clusters_dict.values())
    logging.info(f"聚类完成，共分出 {len(clusters)} 个群组。")
    return clusters

def aggregate_products():
    """
    1. 读取 minimal 清洗后的产品 JSON 数据（键名为 "products_clean"）。
    2. 基于产品的 core_name 进行模糊匹配分群，分群过程中可自动调整相似产品归类（阈值由配置指定）。
    3. 对每个聚类组，选取第一条记录作为代表，聚合该组内所有产品（后续可通过 uid 获取详细信息）。
    4. 最终输出包含最新更新时间和所有聚合结果的 JSON 数据。
    """
    input_file = CONFIG.get("input_file")
    output_file = CONFIG.get("output_file")
    
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info(f"成功读取输入文件: {input_file}")
    except Exception as e:
        logging.error(f"读取 {input_file} 失败: {e}")
        return

    # 使用 "products_clean" 作为数据源
    if "products_clean" in data:
        products = data.get("products_clean", [])
    elif "products" in data:
        products = data.get("products", [])
    else:
        logging.error("无法找到产品数据（未发现 'products_clean' 或 'products' 键）")
        return

    total = len(products)
    if total == 0:
        logging.warning("没有产品数据可进行聚合。")
        return

    logging.info(f"开始进行模糊匹配分群，共 {total} 条产品数据，设置阈值 = {CONFIG.get('similarity_threshold')}")
    clusters = cluster_products_union_find(products, threshold=CONFIG.get("similarity_threshold"))
    
    # 构造聚合结果，每个聚类的代表选择组内第一条数据
    aggregated = []
    for cluster in clusters:
        rep = cluster[0]
        aggregated_record = {
            "uid": rep.get("uid"),
            "core_name": rep.get("core_name", ""),
            "aggregated_products": cluster
        }
        aggregated.append(aggregated_record)

    output_data = {
        "update_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "aggregated_products": aggregated
    }
    
    if CONFIG.get("backup") and os.path.exists(output_file):
        backup_file(output_file, CONFIG.get("backup_dir"))
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        logging.info(f"聚合结果已写入 {output_file}")
    except Exception as e:
        logging.error(f"写入 {output_file} 失败: {e}")

if __name__ == "__main__":
    aggregate_products()