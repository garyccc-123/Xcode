import os
import re
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------
# 用 Selenium 抓取單個商品詳細資訊
def fetch_product_detail(driver, url, timeout=15):
    """
    使用傳入的 Selenium driver 抓取商品詳細資訊。
    回傳 dict = {
      'url', 'name', 'price', 'offer', 'date', 'image_url'
    }
    如果抓取失敗或 name/price 仍是 (無法擷取)，直接回傳 None 表示要丟棄
    """
    # 先預設一個結果（若真的成功才會覆蓋）
    data = {
        "url": url,
        "name": "(無法擷取)",
        "price": "(無法擷取)",
        "offer": "(無)",
        "date": time.strftime("%d/%m/%Y", time.localtime()),
        "image_url": None,
    }
    
    # 嘗試載入
    try:
        driver.get(url)
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-details-container")))
    except Exception as e:
        print(f"[失敗] 載入商品頁失敗: {url}, 錯誤: {e}")
        return None  # 直接放棄此商品
    
    # 商品名稱
    try:
        title_elem = driver.find_element(By.CSS_SELECTOR, "div.info-content .title")
        data["name"] = title_elem.text.strip()
    except Exception as e:
        print(f"[DEBUG] 取得品名失敗: {url}, 錯誤: {e}")

    # 商品價格
    try:
        price_elem = driver.find_element(By.CSS_SELECTOR, "div.info-content .price-line .price")
        data["price"] = price_elem.text.strip()
    except Exception as e:
        print(f"[DEBUG] 取得價格失敗: {url}, 錯誤: {e}")

    # 取得促銷資訊
    try:
        offer_section = driver.find_element(By.CSS_SELECTOR, "div.offer-content")
        offer_items = offer_section.find_elements(By.CSS_SELECTOR, "div.offer-item")
        offer_list = []
        for off in offer_items:
            try:
                tag_text = off.find_element(By.CSS_SELECTOR, "div.tag").text.strip()
                info_text = off.find_element(By.CSS_SELECTOR, "div.info").text.strip()
                offer_list.append(f"【{tag_text}】{info_text}")
            except Exception as e:
                print(f"[DEBUG] 解析促銷項目失敗: {url}, {e}")
        data["offer"] = "; ".join(offer_list) if offer_list else "(無特別促銷)"
    except Exception as e:
        # 無促銷區塊
        data["offer"] = "(無特別促銷)"

    # 取得圖片 URL
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.preview-wrapper div.small img")))
        time.sleep(1)  # 額外等待以確保圖片載入
        img_elem = driver.find_element(By.CSS_SELECTOR, "div.preview-wrapper div.small img")
        data["image_url"] = img_elem.get_attribute("src")
    except Exception as e:
        print(f"[DEBUG] 找不到圖片 <img>: {url}, 錯誤: {e}")
    
    # 如果 name 或 price 還是 (無法擷取)，就棄掉
    if data["name"] == "(無法擷取)" or data["price"] == "(無法擷取)":
        print(f"[棄掉] 抓到的商品資料不完整: {url}")
        return None
    
    # 否則回傳 data
    return data

# -------------------------------
def process_batch(batch_links):
    driver_path = "/opt/homebrew/bin/chromedriver"  # 修改為你的 chromedriver 路徑
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 60)

    batch_results = []
    for url in batch_links:
        result = fetch_product_detail(driver, url)
        if result is not None:
            batch_results.append(result)
        else:
            # 如果是 None, 表示失敗或資料不完整, 就不加入
            pass
    driver.quit()
    return batch_results

# -------------------------------
def scrape_category_links(url_template):
    driver_path = "/opt/homebrew/bin/chromedriver"  # 修改為你的 chromedriver 路徑
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 60)
    
    current_page = 1
    all_links = []
    try:
        while True:
            page_url = url_template.format(current_page)
            print(f"[列表] {page_url}")
            driver.get(page_url)
            try:
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row-container")))
            except Exception as e:
                print(f"第 {current_page} 頁載入失敗或無 row-container: {e}")
                break

            row_containers = driver.find_elements(By.CSS_SELECTOR, "div.row-container")
            page_links = []
            for row in row_containers:
                link_elems = row.find_elements(By.CSS_SELECTOR, "a.ware-wrapper")
                for link in link_elems:
                    href = link.get_attribute("href")
                    if href:
                        page_links.append(href)
            if not page_links:
                print(f"第 {current_page} 頁沒有商品，結束翻頁。")
                break

            all_links.extend(page_links)
            print(f"第 {current_page} 頁抓到 {len(page_links)} 筆連結，累計 {len(all_links)} 筆。")
            
            # 檢查是否有下一頁按鈕
            try:
                driver.find_element(By.LINK_TEXT, "下一頁")
                current_page += 1
                time.sleep(1)
            except Exception:
                print("沒有下一頁，結束翻頁。")
                break
    finally:
        time.sleep(1)
        driver.quit()
    return all_links

# -------------------------------
def scrape_and_merge_all_categories():
    categories = {
        "酒類": "https://www.wellcome.com.hk/zh-hant/category/100001/{}.html",
        "早餐/麵包": "https://www.wellcome.com.hk/zh-hant/category/100003/{}.html",
        "罐頭/湯": "https://www.wellcome.com.hk/zh-hant/category/100004/{}.html",
        "日用品": "https://www.wellcome.com.hk/zh-hant/category/100013/{}.html",
        "乳製品/冷凍食品/蛋": "https://www.wellcome.com.hk/zh-hant/category/100007/{}.html",
        "飲料": "https://www.wellcome.com.hk/zh-hant/category/100002/{}.html",
        "冷凍食品": "https://www.wellcome.com.hk/zh-hant/category/100010/{}.html",
        "水果/蔬菜": "https://www.wellcome.com.hk/zh-hant/category/100011/{}.html",
        "糧油": "https://www.wellcome.com.hk/zh-hant/category/100020/{}.html",
        "肉類": "https://www.wellcome.com.hk/zh-hant/category/100015/{}.html",
        "調味料及醬料": "https://www.wellcome.com.hk/zh-hant/category/100005/{}.html",
        "零食": "https://www.wellcome.com.hk/zh-hant/category/100022/{}.html",
    }
    
    merged_products = {}
    
    for category_name, url_template in categories.items():
        print(f"開始抓取分類：{category_name}")
        product_links = scrape_category_links(url_template)
        print(f"{category_name} 分類共抓取到 {len(product_links)} 筆連結")
        
        # 分批
        batch_size = 20
        batches = [product_links[i:i+batch_size] for i in range(0, len(product_links), batch_size)]
        print(f"{category_name} 分類共拆分為 {len(batches)} 批，每批最多 {batch_size} 個連結")
        
        # 多執行緒
        MAX_WORKERS = min(40, len(batches))
        all_data = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_batch, batch): batch for batch in batches}
            for future in as_completed(futures):
                batch_results = future.result()
                all_data.extend(batch_results)
        print(f"{category_name} 分類已抓取有效商品：{len(all_data)} 筆（已排除載入失敗或無效資料）")
        
        # 合併結果：帶有「多筆歷史」結構
        for product in all_data:
            product_url = product["url"]
            if product_url not in merged_products:
                merged_products[product_url] = {
                    "url": product_url,
                    "categories": [],
                    "history": []
                }
            # 加入分類
            if category_name not in merged_products[product_url]["categories"]:
                merged_products[product_url]["categories"].append(category_name)
            
            # 建立此筆更新的 record
            new_record = {
                "name": product["name"],
                "price": product["price"],
                "offer": product["offer"],
                "date": product["date"],
                "image_url": product["image_url"]
            }
            merged_products[product_url]["history"].append(new_record)
            
            # 在最外層同步一份最新
            merged_products[product_url]["name"] = new_record["name"]
            merged_products[product_url]["price"] = new_record["price"]
            merged_products[product_url]["offer"] = new_record["offer"]
            merged_products[product_url]["date"] = new_record["date"]
            merged_products[product_url]["image_url"] = new_record["image_url"]
    
    merged_list = list(merged_products.values())
    
    # 加入整體更新日期
    update_date = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    output = {
        "update_date": update_date,
        "products": merged_list
    }
    return output

if __name__ == "__main__":
    start_time = time.time()
    result = scrape_and_merge_all_categories()
    merged_products_list = result["products"]
    output_file = "combined_products.json"
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"合併的產品資料已寫入 {output_file}，products 數量：{len(merged_products_list)}")
    except Exception as e:
        print(f"寫入 {output_file} 失敗: {e}")
    
    end_time = time.time()
    print(f"總耗時: {end_time - start_time:.2f} 秒")
