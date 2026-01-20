import os
import re
import json
import time
import requests
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------
# 使用 Selenium 抓取單個商品詳細資訊（中文版），並轉跳英文頁面取得英文商品名稱
def fetch_product_detail(driver, url, timeout=15):
    """
    使用傳入的 Selenium driver 抓取商品詳細資訊（中文版），
    並自動轉跳到英文頁面取得英文商品名稱。
    回傳 dict 包含:
      'url', 'name', 'price', 'offer', 'date', 'image_url', 'product_eng_name'
    如果抓取失敗或 name/price 仍是 (無法擷取)，則回傳 None 表示要丟棄該商品。
    """
    # 預設結果（成功後會覆蓋）
    data = {
        "url": url,
        "name": "(無法擷取)",
        "price": "(無法擷取)",
        "offer": "(無)",
        "date": time.strftime("%d/%m/%Y", time.localtime()),
        "image_url": None,
        "product_eng_name": "(尚未取得英文名稱)"
    }
    
    # 嘗試載入中文版商品頁
    try:
        driver.get(url)
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-details-container")))
    except Exception as e:
        print(f"[失敗] 載入商品頁失敗: {url}, 錯誤: {e}")
        return None  # 放棄此商品
    
    # 取得商品名稱（中文版）
    try:
        title_elem = driver.find_element(By.CSS_SELECTOR, "div.info-content .title")
        data["name"] = title_elem.text.strip()
    except Exception as e:
        print(f"[DEBUG] 取得品名失敗: {url}, 錯誤: {e}")
    
    # 取得商品價格
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
        data["offer"] = "(無特別促銷)"
    
    # 取得圖片 URL
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.preview-wrapper div.small img")))
        time.sleep(1)  # 額外等待以確保圖片載入
        img_elem = driver.find_element(By.CSS_SELECTOR, "div.preview-wrapper div.small img")
        data["image_url"] = img_elem.get_attribute("src")
    except Exception as e:
        print(f"[DEBUG] 找不到圖片 <img>: {url}, 錯誤: {e}")
    
    # 如果名稱或價格仍無法取得，則放棄此商品
    if data["name"] == "(無法擷取)" or data["price"] == "(無法擷取)":
        print(f"[棄掉] 抓到的商品資料不完整: {url}")
        return None

    # -------------------------------
    # 新增部分：轉跳英文頁面並取得英文商品名稱
    eng_url = url.replace("zh-hant", "en")
    print(f"[INFO] 嘗試載入英文頁面: {eng_url}")
    try:
        driver.get(eng_url)
        # 延長等待時間確保英文頁面穩定載入
        wait = WebDriverWait(driver, timeout + 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.info-content .title")))
        english_title_elem = driver.find_element(By.CSS_SELECTOR, "div.info-content .title")
        eng_name = english_title_elem.text.strip()
        if eng_name:
            print(f"[INFO] 英文商品名稱取得: {eng_name}")
        else:
            print(f"[WARN] 英文頁面名稱為空: {eng_url}")
        data["product_eng_name"] = eng_name
    except Exception as e:
        print(f"[DEBUG] 取得英文名稱失敗: {eng_url}, 錯誤: {e}")
        data["product_eng_name"] = "(無法擷取英文名稱)"
    
    return data

# -------------------------------
# 對一批商品連結進行處理，使用同一個 headless driver
def process_batch(batch_links, main_cat, sub_cat):
    driver_path = "/opt/homebrew/bin/chromedriver"  # 修改為您的 chromedriver 路徑
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 60)

    batch_success = []
    batch_fail = []
    for url in batch_links:
        result = fetch_product_detail(driver, url)
        if result is not None:
            # 成功時加入 main_category 與 sub_category
            result["main_category"] = main_cat
            result["sub_category"] = sub_cat
            batch_success.append(result)
        else:
            # 失敗 -> 保存基本信息 (url, main_category, sub_category)
            fail_info = {
                "url": url,
                "main_category": main_cat,
                "sub_category": sub_cat
            }
            batch_fail.append(fail_info)
    driver.quit()
    return (batch_success, batch_fail)

# -------------------------------
# 利用 Selenium 取得分類頁面中所有商品連結
def scrape_category_links(url_template):
    def use_b_method(url):
        return "search?keyword=" in url

    driver_path = "/opt/homebrew/bin/chromedriver"
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
            if use_b_method(url_template):
                page_url = re.sub(r"page=\d+", f"page={current_page}", url_template)
            else:
                page_url = re.sub(r'/\d+\.html$', f'/{current_page}.html', url_template)

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

            if "search?keyword=" in url_template:
                print(f"[DEBUG] 使用 B 方法翻頁，當前頁碼: {current_page}")
                try:
                    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.next.cursor.btn-box.op-btn")))
                    driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
                    next_btn.click()
                    current_page += 1
                    time.sleep(2)
                except Exception as e:
                    print(f"[DEBUG] 點擊下一頁失敗，錯誤信息: {e}")
                    break
            else:
                try:
                    driver.find_element(By.LINK_TEXT, "下一頁").click()
                    current_page += 1
                    time.sleep(1)
                except Exception as e:
                    print(f"分類頁：找不到或點擊下一頁按鈕失敗: {e}")
                    break
    finally:
        time.sleep(1)
        driver.quit()
    return list(set(all_links))

# -------------------------------
# 主函式：兩層分類抓取並合併資料
def scrape_and_merge_all_categories():
    """
    主函式：兩層 (main_category → sub_category) 迴圈抓取，將成功/失敗分別寫成 JSON。
    """
    # 二階層 categories (main_cat -> sub_cat -> [多個網址])
    categories = {
    "水果/蔬菜": {
        "水果": [
            "https://www.wellcome.com.hk/zh-hant/category/100011-100133/1.html"
        ],
        "蔬菜": [
            "https://www.wellcome.com.hk/zh-hant/category/100011-100135/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100011-100140-100883/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100011-100140-100887/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100011-100140-100884/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100011-100140-100880/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100011-100139/1.html"
        ]
    },

    "飲品": {
        "汽水": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100067/1.html"
        ],
        "即飲茶類、咖啡、奶茶": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100066/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100061-100480/1.html"
        ],
        "奶類、乳酪飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100063/3.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100071-100542/1.html"
        ],
        "植物奶、大豆飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100071-100541/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100071-100539/1.html"
        ],
        "沖調飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100069-100529/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100069-100522/2.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100061-100479/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100061-100470/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100002-100061-100474/1.html"
        ],
        "果汁": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100064/1.html"
        ],
        "運動及能量飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100068/1.html"
        ],
        "涼茶": [
            "https://www.wellcome.com.hk/zh-hant/category/100002-100066-100504/1.html"
        ],
        "原箱飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/105591-105786/1.html"
        ]
    },

    "酒精飲品": {
        "啤酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100044/1.html"
        ],
        "蘋果酒、果酒、雞尾酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100047/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100001-100054-100432/1.html"
        ],
        "紅酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100051/1.html"
        ],
        "白酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100055/1.html"
        ],
        "香檳、有氣酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100045/1.html"
        ],
        "氈酒、甜酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100054-100433/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100001-100054-100435/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100001-100054-100434/1.html"
        ],
        "白蘭地、干邑": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100054-100431/1.html"
        ],
        "清酒、燒酒、果味米酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100048/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100001-100049/1.html"
        ],
        "無酒精酒": [
            "https://www.wellcome.com.hk/zh-hant/category/100001-100044-100389/1.html"
        ]
    },

    "糧油": {
        "米": [
            "https://www.wellcome.com.hk/zh-hant/category/100020/1.html"
        ],
        "即食粉麵/飯": [
            "https://www.wellcome.com.hk/zh-hant/category/100020-100244-101353/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100020-100243/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100020-100240/1.html"
        ],
        "油": [
            "https://www.wellcome.com.hk/zh-hant/category/100020-100242/1.html"
        ],
        "麵粉、烘焙用料、梳打粉": [
            "https://www.wellcome.com.hk/zh-hant/category/100005-100090-100648/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100090-100649/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100090-100650/1.html"
        ]
    },

    "零食": {
        "餅乾、曲奇": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100254/1.html"
        ],
        "薯片、蝦片、爆谷": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100259/1.html"
        ],
        "朱古力、糖果、香口膠": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100255/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-100262/1.html"
        ],
        "果乾、果仁、紫菜": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-105961/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101427/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101423/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101434/1.html"
        ],
        "魚肉腸、肉乾": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101426/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101430/1.html"
        ],
        "蛋卷、糕點": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101420/1.html"
        ],
        "布丁、啫喱、糖水": [
            "https://www.wellcome.com.hk/zh-hant/category/100022-100260-101432/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100022-106176/1.html"
        ]
    },

    "調味料、醬料": {
        "鹽、糖、其他調味料": [
            "https://www.wellcome.com.hk/zh-hant/category/100005-100091-100654/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100091-100656/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100091-100653/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100091-100652/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100091-100655/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100090-100651/1.html"
        ],
        "豉油": [
            "https://www.wellcome.com.hk/zh-hant/category/100005-100089-100645/1.html"
        ],
        "醬料": [
            "https://www.wellcome.com.hk/zh-hant/category/100005-100089-100637/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100089-100644/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100089-100641/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100089-100643/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100634/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100635/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100632/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100629/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100627/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100636/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100630/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100005-100088-100628/1.html"
        ]
    },

    "罐頭": {
        "罐頭肉": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100596/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100587/1.html"
        ],
        "罐頭海鮮": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100584/1.html"
        ],
        "罐頭鮑魚": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100589/1.html"
        ],
        "罐頭水果": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100585/1.html"
        ],
        "罐頭湯": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100590/1.html"
        ],
        "罐頭蔬菜、豆": [
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100583/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100004-100082-100592/1.html"
        ]
    },

    "早餐、果醬": {
        "麵包糕點": [
            "https://www.wellcome.com.hk/zh-hant/category/100003-100075/1.html"
        ],
        "燕麥、穀類": [
            "https://www.wellcome.com.hk/zh-hant/category/100003-100076/1.html"
        ],
        "果醬": [
            "https://www.wellcome.com.hk/zh-hant/category/100003-100080/1.html"
        ]
    },

    "冷凍食品(乳製品,豆製品,蛋類)": {
        "蛋類": [
            "https://www.wellcome.com.hk/zh-hant/category/100007-100108/1.html"
        ],
        "豆製品": [
            "https://www.wellcome.com.hk/zh-hant/category/100007-100115/1.html"
        ],
        "乳製品": [
            "https://www.wellcome.com.hk/zh-hant/category/100007-100098/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100007-100110/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100007-100097-100672/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100007-100109/1.html"
        ],
        "冷凍飲品": [
            "https://www.wellcome.com.hk/zh-hant/category/100007-100103/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100007-100110/1.html"
        ]
    },

    "急凍食品": {
        "急凍海鮮": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100187/1.html"
        ],
        "急凍肉類": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101117/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101116/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101108/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101113/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101109/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101115/1.html"
        ],
        "丸類、冷盤": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100186-101114/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100007-100111-100739/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100015-100182-101095/1.html"
        ],
        "餃子、雲吞": [
            "https://www.wellcome.com.hk/zh-hant/category/100003-100079-100572/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100003-100079-100573/1.html"
        ],
        "點心、湯丸": [
            "https://www.wellcome.com.hk/zh-hant/category/100003-100079-100571/1.html"
        ],
        "薄餅、急凍小食": [
            "https://www.wellcome.com.hk/zh-hant/category/100010-100122-100783/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100010-100122-100786/1.html"
        ],
        "急凍麵食、年糕": [
            "https://www.wellcome.com.hk/zh-hant/category/100010-100122-100781/1.html"
        ]
    },

    "肉類": {
        "牛肉": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100182-101090/1.html"
        ],
        "豬肉": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100182-101093/1.html"
        ],
        "家禽": [
            "https://www.wellcome.com.hk/zh-hant/category/100015-100182-101094/1.html"
        ]
    },

    "個人護理": {
        "牙膏": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100027-100289/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100000-100027-100288/1.html"
        ],
        "漱口水": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100027-100287/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100000-100027-100286/1.html"
        ],
        "沐浴露": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100023-100266/1.html"
        ],
        "防曬用品": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100042-100381/1.html"
        ],
        "止汗、香體用品": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100029/1.html"
        ],
        "潤膚產品": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100023-100267/1.html"
        ],
        "洗髮水": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100033-100336/1.html"
        ],
        "護髮素": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100033-100329/1.html"
        ],
        "修護、焗油、精華": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100033-100330/1.html"
        ],
        "洗手液": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100023-100273/1.html"
        ]
    },

    "女士衛生護理": {
        "衛生巾、護墊": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100032-100325/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100000-100032-100324/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100000-100032-100326/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100000-100032-100328/1.html"
        ],
        "女士衛生潔膚液": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100032-100327/1.html"
        ]
    },

    "剃鬚用品": {
        "剃鬚刀": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100036-100345/1.html"
        ],
        "補充刀片": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E5%88%80%E9%A0%AD&page=1"
        ],
        "剃鬚膏、泡沫、啫喱": [
            "https://www.wellcome.com.hk/zh-hant/category/100000-100036-100346/1.html"
        ]
    },

    "紙巾": {
        "廁紙、卷紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100174-101065/1.html"
        ],
        "盒裝紙巾、抹手紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100174-101061/1.html"
        ],
        "廚房紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100174-101062/1.html"
        ],
        "紙手巾": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E7%B4%99%E6%89%8B%E5%B7%BE&page=1"
        ],
        "清潔濕紙巾": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E6%B8%85%E6%BD%94%E6%BF%95%E7%B4%99%E5%B7%BE&page=1"
        ],
        "濕紙巾及濕廁紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100174-101067/1.html"
        ]
    },

    "家居清潔": {
        "漂白水、清潔劑": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100165-101003/1.html"
        ],
        "清潔工具": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100165-101004/1.html"
        ],
        "抽濕用品": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E6%8A%BD%E6%BF%95&page=1"
        ]
    },

    "廚房清潔": {
        "百潔綿布、海綿": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E7%99%BE%E6%BD%94&page=1"
        ],
        "洗潔精": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100171-101040/1.html"
        ],
        "廚房清潔劑": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100165-101011/1.html"
        ]
    },

    "浴室清潔": {
        "潔廁劑": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100165-101001/1.html"
        ],
        "浴室清潔劑": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E6%B5%B4%E5%AE%A4%E6%B8%85%E6%BD%94%E5%8A%91&page=1"
        ],
        "通渠用品": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E9%80%9A%E6%B8%A0&page=1"
        ]
    },

    "洗衣用品": {
        "洗衣液": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101051/1.html"
        ],
        "洗衣粉": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101052/1.html"
        ],
        "洗衣珠、洗衣紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101050/1.html",
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E6%B4%97%E8%A1%A3%E7%B4%99&page=1"
        ],
        "柔順劑": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101046/1.html"
        ],
        "衣物清香、除菌噴霧": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101047/1.html",
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E9%99%A4%E8%8F%8C%E5%99%B4%E9%9C%A7&page=1"
        ],
        "去漬、漂白": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101049/1.html",
            "https://www.wellcome.com.hk/zh-hant/category/100013-100172-101053/1.html"
        ]
    },

    "廚房用品": {
        "食物儲存、保鮮紙": [
            "https://www.wellcome.com.hk/zh-hant/category/100013-100171-101043/1.html"
        ],
        "垃圾袋": [
            "https://www.wellcome.com.hk/zh-hant/search?keyword=%E5%9E%83%E5%9C%BE%E8%A2%8B&page=1"
        ]
    }
}

    merged_products = {}
    fail_products = []

    # 兩層迴圈： main_cat -> sub_cat -> [網址...]
    for main_cat, sub_dict in categories.items():
        for sub_cat, url_list in sub_dict.items():
            all_links = []
            # 針對每個網址呼叫 scrape_category_links
            for single_url in url_list:
                new_links = scrape_category_links(single_url)
                all_links.extend(new_links)
            print(f"\n[{main_cat} - {sub_cat}] 共獲取到 {len(all_links)} 筆商品連結")

            # 分批處理
            batch_size = 20
            batches = [all_links[i:i + batch_size] for i in range(0, len(all_links), batch_size)]
            print(f"分為 {len(batches)} 批, 每批 {batch_size} 個連結")

            all_success = []
            all_fail = []

            # 多執行緒處理
            max_workers = min(40, len(batches))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {
                    executor.submit(process_batch, batch, main_cat, sub_cat): batch
                    for batch in batches
                }
                for future in as_completed(futures):
                    success_list, fail_list = future.result()
                    all_success.extend(success_list)
                    all_fail.extend(fail_list)
            print(f"[{main_cat} - {sub_cat}] 成功 {len(all_success)} 筆, 失敗 {len(all_fail)} 筆")
            
            # 合併成功資料
            for item in all_success:
                product_url = item["url"]
                if product_url not in merged_products:
                    merged_products[product_url] = {
                        "url": product_url,
                        "uid": hashlib.md5(product_url.encode('utf-8')).hexdigest(),
                        "main_category": [],
                        "sub_categories": [],
                        "history": []
                    }
                if main_cat not in merged_products[product_url]["main_category"]:
                    merged_products[product_url]["main_category"].append(main_cat)
                if sub_cat not in merged_products[product_url]["sub_categories"]:
                    merged_products[product_url]["sub_categories"].append(sub_cat)
                new_record = {
                    "name": item["name"],
                    "price": item["price"],
                    "offer": item["offer"],
                    "date": item["date"],
                    "image_url": item["image_url"],
                    "product_eng_name": item["product_eng_name"]
                }
                merged_products[product_url]["history"].append(new_record)
                # 同步最新資料
                merged_products[product_url]["name"] = item["name"]
                merged_products[product_url]["price"] = item["price"]
                merged_products[product_url]["offer"] = item["offer"]
                merged_products[product_url]["date"] = item["date"]
                merged_products[product_url]["image_url"] = item["image_url"]
                merged_products[product_url]["product_eng_name"] = item["product_eng_name"]
            
            # 收集失敗資料
            for fitem in all_fail:
                fail_products.append(fitem)
    
    merged_list = list(merged_products.values())
    output_data = {
        "update_date": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()),
        "products": merged_list
    }
    return output_data, fail_products

# -------------------------------
if __name__ == "__main__":
    start_time = time.time()

    final_data, fail_data = scrape_and_merge_all_categories()

    # 寫入成功檔案: combined_products_wellcom_with_eng.json
    try:
        with open("combined_products_wellcom_with_eng.json", "w", encoding="utf-8") as f:
            json.dump(final_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 成功資訊已寫入 combined_products_wellcom_with_eng.json, products 數量: {len(final_data['products'])}")
    except Exception as e:
        print(f"❌ 寫入 combined_products_wellcom.json 失敗: {e}")

    # 寫入失敗檔案: fail_products.json
    try:
        with open("fail_products.json", "w", encoding="utf-8") as f:
            json.dump(fail_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 失敗資訊已寫入 fail_products.json, 失敗數量: {len(fail_data)}")
    except Exception as e:
        print(f"❌ 寫入 fail_products.json 失敗: {e}")

    end_time = time.time()
    print(f"總耗時: {end_time - start_time:.2f} 秒")
