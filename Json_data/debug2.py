import json

# 請確保這些路徑與您原本腳本中的 INPUT_FILES 一致
FILES_TO_CHECK = [
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_pns_with_eng.json',
    '/Users/gary/Documents/Supermarket1/Json_data/combined_products_wellcom_with_eng.json'
]

def check_json_files():
    for file_path in FILES_TO_CHECK:
        print(f"正在檢查: {file_path} ...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # 嘗試讀取
                content = f.read()
                json.loads(content)
            print("✅ 格式正確")
        except json.JSONDecodeError as e:
            print(f"❌ 格式錯誤！")
            print(f"   錯誤原因: {e.msg}")
            print(f"   錯誤位置: 第 {e.lineno} 行, 第 {e.colno} 列")
            print(f"   (字元位置: {e.pos})")
            
            # 嘗試印出錯誤附近的內容幫助除錯
            start = max(0, e.pos - 50)
            end = min(len(content), e.pos + 50)
            snippet = content[start:end]
            print(f"   錯誤附近內容: ...{snippet}...")
        except FileNotFoundError:
            print(f"❌ 找不到檔案")

if __name__ == "__main__":
    check_json_files()