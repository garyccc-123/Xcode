

import argparse
import json
import logging
import os
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple



def slug(text: str) -> str:
    """將任何字串轉成檔名安全的 slug (ASCII & 下劃線)."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text) or "unknown"


def guess_brand(prod_eng_name: str) -> str:
    """
    粗略以產品英文名的第一個單字當作「品牌」，
    若不存在就回傳 'unknown_brand'。
    """
    first_token = prod_eng_name.split()[0] if prod_eng_name else ""
    return first_token.lower() if first_token.isalpha() else "unknown_brand"


def validate_product(p: Dict) -> Tuple[bool, str]:
    """確認必要欄位皆存在且非空；失敗時回傳 False 及原因。"""
    required = ["uid", "product_eng_name_clean", "core_name"]
    for k in required:
        if not p.get(k):
            return False, f"缺少欄位: {k}"
    return True, ""


###############################################################################
# ──────── 主處理流程 ─────────────────────────────────────────────────────── #
###############################################################################


def group_products(
    products: List[Dict], keep_chinese_file: bool = False
) -> Dict[str, List[Dict]]:
    """
    依 sub-category 與品牌分桶：
        key 格式 ＝ 〈subcat_slug〉__〈brand_slug〉
    只保留 uid 與 product_eng_name_clean 兩欄。
    """
    buckets: Dict[str, List[Dict]] = defaultdict(list)

    for idx, p in enumerate(products, 1):
        ok, err = validate_product(p)
        if not ok:
            logging.warning("第 %d 筆資料無效：%s；已跳過", idx, err)
            continue

        subcat = (p.get("sub_categories") or ["未分類"])[0]
        brand = guess_brand(p["product_eng_name_clean"])

        file_key = f"{subcat}__{brand}"
        if not keep_chinese_file:
            file_key = f"{slug(subcat)}__{slug(brand)}"

        buckets[file_key].append(
            {
                "uid": p["uid"],
                "product_eng_name_clean": p["product_eng_name_clean"],
            }
        )
    return buckets


def save_buckets(buckets: Dict[str, List[Dict]], out_dir: Path) -> None:
    """將每個分桶寫成 JSON。"""
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for key, items in buckets.items():
        out_path = out_dir / f"{key}.json"
        payload = {"update_date": ts, "products": items}

        with out_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        logging.info("已輸出 %-40s (%4d 筆)", out_path.name, len(items))


###############################################################################
# ──────── CLI & main ──────────────────────────────────────────────────────── #
###############################################################################


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean & bucket products JSON")
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="輸入 JSON 路徑 (all_data_clean_minimal.json)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        required=True,
        help="分桶後 JSON 的輸出資料夾",
    )
    parser.add_argument(
        "--keep-chinese",
        action="store_true",
        help="檔名保留中文 (預設轉 slug)",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="日誌等級 (default: INFO)",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> None:
    args = parse_args(argv)

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    input_path = Path(args.input)
    if not input_path.is_file():
        logging.error("找不到輸入檔：%s", input_path)
        sys.exit(1)

    logging.info("開始載入 %s …", input_path)
    with input_path.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    products = raw.get("products_clean", [])
    logging.info("載入產品總數：%d", len(products))

    buckets = group_products(products, keep_chinese_file=args.keep_chinese)
    logging.info("分桶完成，總桶數：%d", len(buckets))

    save_buckets(buckets, Path(args.output_dir))
    logging.info("所有分桶已寫入 %s", args.output_dir)


if __name__ == "__main__":
    main(sys.argv[1:])