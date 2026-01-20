import csv
import json
import requests
import time

# 输入 CSV 文件名（请确保文件在脚本所在目录或提供完整路径）
INPUT_CSV = 'store_location.csv'
# 输出 JSON 文件名
OUTPUT_JSON = 'stores_with_coords.json'

def geocode_address(address):
    """
    调用 OpenStreetMap 的 Nominatim API 根据地址获取经纬度数据
    """
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    # 设置请求头，User-Agent 建议填写你的 App 名称或联系邮箱
    headers = {
        "User-Agent": "SupermarketApp/1.0 (gary_05002@gmail.com)"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
    except Exception as e:
        print(f"请求地址 '{address}' 失败：{e}")
        return None, None

    if response.status_code == 200:
        data = response.json()
        if data:
            try:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                return lat, lon
            except (KeyError, ValueError) as e:
                print(f"解析地址 '{address}' 数据出错：{e}")
                return None, None
        else:
            print(f"地址 '{address}' 未找到结果")
            return None, None
    else:
        print(f"HTTP 错误 {response.status_code}：{response.text}")
        return None, None

def main():
    stores = []
    # 读取 CSV 文件
    with open(INPUT_CSV, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            address = row.get('address', '').strip()
            print("正在处理地址:", address)
            if address:
                lat, lon = geocode_address(address)
                # 如果无法获取经纬度，默认设置为 0.0
                row['latitude'] = lat if lat is not None else 0.0
                row['longitude'] = lon if lon is not None else 0.0
            else:
                row['latitude'] = 0.0
                row['longitude'] = 0.0
            stores.append(row)
            # 为避免超过 API 请求频率限制，每次请求后等待 1 秒
            time.sleep(1)
    
    # 将结果写入 JSON 文件
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as jsonfile:
        json.dump(stores, jsonfile, ensure_ascii=False, indent=4)
    
    print(f"完成！共处理 {len(stores)} 家门店数据，并保存到 {OUTPUT_JSON}")

if __name__ == "__main__":
    main()