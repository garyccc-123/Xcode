#!/usr/bin/env python3
# test_write.py

import os
import json
from datetime import datetime

def main():
    # 印出目前工作目錄，確認路徑
    cwd = os.getcwd()
    print(f"🔍 Current working directory: {cwd}")

    # 要寫入的測試資料
    test_data = {
        "ok": True,
        "timestamp": datetime.now().isoformat()
    }

    # 寫入 test_write.json
    out_filename = "test_write.json"
    out_path = os.path.join(cwd, out_filename)
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Successfully wrote {out_filename} at:\n   {out_path}")
    except Exception as e:
        print(f"❌ Failed to write {out_filename}: {e}")

if __name__ == "__main__":
    main()