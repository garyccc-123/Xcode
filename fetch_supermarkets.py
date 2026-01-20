import requests
import json
import time

# 定義 API 金鑰
API_KEY = 'AIzaSyC5e50EykoQ80b8LZD4APpqSVVaRGbf9yg'  # 請替換為你的 Google API 金鑰
QUERY = '百佳'
LOCATION = '22.3,114.2'  # 設置搜尋範圍為香港地區
RADIUS = 50000  # 增加搜尋範圍為 50 公里

# 創建一個空的列表來儲存超市資料
stores = []

# 初始的 API 請求 URL
url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={QUERY}&location={LOCATION}&radius={RADIUS}&key={API_KEY}'

# 定義一個函數來獲取資料
def get_data(url):
    try:
        print(f"發送請求到 Google Places API: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print("請求成功，正在處理資料...")
            return response.json()
        else:
            print(f"請求失敗，HTTP 狀態碼: {response.status_code}")
            return None
    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

# 獲取詳細資料
def get_place_details(place_id):
    details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}'
    print(f"請求詳細資料: {details_url}")
    response = requests.get(details_url)
    if response.status_code == 200:
        data = response.json()
        result = data.get('result', {})
        phone_number = result.get('formatted_phone_number', 'N/A')
        opening_hours = result.get('opening_hours', {}).get('weekday_text', 'N/A')
        return phone_number, opening_hours
    else:
        print(f"無法獲取詳細資料，HTTP 狀態碼: {response.status_code}")
        return 'N/A', 'N/A'

# 獲取資料並處理每一頁結果
while url:
    print(f"正在請求資料: {url}")
    data = get_data(url)
    
    if data is None:
        print("無法獲取資料，結束程式")
        break

    # 顯示完整的回應資料
    print("API 回應資料:", json.dumps(data, ensure_ascii=False, indent=4))
    
    # 處理每一個結果並將其轉換為所需的 JSON 格式
    for place in data.get('results', []):
        store_name = place.get('name', 'N/A')
        address = place.get('formatted_address', 'N/A')
        latitude = place['geometry']['location'].get('lat', 'N/A')
        longitude = place['geometry']['location'].get('lng', 'N/A')
        place_id = place.get('place_id', '')
        
        # 獲取詳細資料：電話號碼和營業時間
        phone_number, opening_hours = get_place_details(place_id)
        
        # 儲存到字典中
        store_data = {
            "名称": store_name,
            "地址": address,
            "电话": phone_number,
            "营业时间": opening_hours,
            "latitude": latitude,
            "longitude": longitude,
        }
        
        # 將字典添加到列表中
        stores.append(store_data)
    
    # 檢查是否有下一頁
    if 'next_page_token' in data:
        print("正在獲取下一頁資料...")
        next_page_token = data['next_page_token']
        url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={API_KEY}'
        time.sleep(2)  # 等待 2 秒鐘再請求下一頁
    else:
        print("所有資料已經獲取完畢。")
        url = None

# 將結果儲存為 JSON 格式
if stores:
    with open('supermarkets.json', 'w', encoding='utf-8') as json_file:
        json.dump(stores, json_file, ensure_ascii=False, indent=4)
    print("JSON 文件已成功創建！")
else:
    print("未獲取到任何資料。")