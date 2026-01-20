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

driver_path = "/opt/homebrew/bin/chromedriver"
output_folder = "Wellcome_Alcohol"
os.makedirs(output_folder, exist_ok=True)

def fetch_product_detail(driver, url, timeout=15):
    wait = WebDriverWait(driver, timeout)
    data = {
        "url": url,
        "name": "(無法擷取)",
        "price": "(無法擷取)",
        "offer": "(無促銷區塊)",
        "date": time.strftime("%d/%m/%Y"),
        "image_url": None
    }
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-details-container")))
        
        data["name"] = driver.find_element(By.CSS_SELECTOR, "div.info-content .title").text.strip()
        data["price"] = driver.find_element(By.CSS_SELECTOR, "div.info-content .price-line .price").text.strip()

        offer_section = driver.find_elements(By.CSS_SELECTOR, "div.offer-content .offer-item")
        offers = []
        for offer in offer_section:
            tag = offer.find_element(By.CSS_SELECTOR, "div.tag").text.strip()
            info = offer.find_element(By.CSS_SELECTOR, "div.info").text.strip()
            offers.append(f"【{tag}】{info}")
        data["offer"] = "; ".join(offers) if offers else "(無特別促銷)"

        img_elem = driver.find_element(By.CSS_SELECTOR, "div.preview-wrapper div.small img")
        data["image_url"] = img_elem.get_attribute("src")

    except Exception as e:
        print(f"擷取商品詳情錯誤：{url}，錯誤訊息：{e}")

    return data

def download_image(img_url, file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Referer": "https://www.wellcome.com.hk/"
    }
    try:
        response = requests.get(img_url, headers=headers, timeout=10, verify=False)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"圖片已下載：{file_path}")
        else:
            print(f"圖片下載失敗（狀態碼：{response.status_code}）：{img_url}")
    except Exception as e:
        print(f"圖片下載錯誤：{img_url}，錯誤訊息：{e}")

def safe_filename(name):
    # 只保留中文
    return re.sub(r'[^一-龥]', '', name) or "未知商品"

def task_fetch(url):
    driver_path = "/opt/homebrew/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    sub_driver = webdriver.Chrome(service=Service(driver_path), options=options)
    detail = fetch_product_detail(sub_driver, url)
    sub_driver.quit()
    return detail

def scrape_wellcome_each_json_append_with_image():
    driver_path = "/opt/homebrew/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    wait = WebDriverWait(driver, 10)

    output_folder = "Wellcome_Alcohol"
    os.makedirs(output_folder, exist_ok=True)

    base_url = "https://www.wellcome.com.hk/zh-hant/category/100001/{}.html"
    current_page = 1
    all_links = []

    try:
        while True:
            url = base_url.format(current_page)
            print(f"抓取第 {current_page} 頁：{url}")
            driver.get(url)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.row-container")))

            link_elements = driver.find_elements(By.CSS_SELECTOR, "div.row-container a.ware-wrapper")
            if not link_elems:
                break

            for link in link_elems:
                href = link.get_attribute("href")
                all_links.append(href)

            try:
                driver.find_element(By.LINK_TEXT, "下一頁")
                current_page += 1
            except:
                break
    finally:
        driver.quit()

    print(f"總共找到 {len(all_links)} 個商品連結，開始多執行緒抓取。")

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task_fetch, link) for link in all_links]
        for future in as_completed(futures):
            new_data = future.result()
            results.append(new_data)

    for idx, item in enumerate(results, start=1):
        safe_name = re.sub(r'[^一-龥]', '', item['name']) or f"未命名商品{idx}"

        json_path = os.path.join(output_folder, f"{safe_name}.json")
        old_list = []

        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                old_list = json.load(f)
        else:
            old_list = []

        old_list.append(item)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(old_list, f, ensure_ascii=False, indent=2)

        img_url = item.get("image_url")
        if img_url:
            img_path = os.path.join(output_folder, f"{safe_name}.jpg")
            if not os.path.exists(img_path):
                download_image(img_url, img_path)
            else:
                print(f"[{idx}] 圖片已存在，跳過下載：{img_path}")

        print(f"[{idx}] 已追加 JSON：{json_path}（當前共 {len(old_list)} 筆）")

if __name__ == "__main__":
    scrape_wellcome_each_json_append_with_image()



