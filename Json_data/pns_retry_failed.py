import json
import time
from datetime import datetime
import concurrent.futures
import hashlib  # For UID generation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = "/opt/homebrew/bin/chromedriver"  # Adjust this path as needed

def init_driver():
    """初始化 Chrome 瀏覽器 (需與主爬蟲的做法一致)"""
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 如需無頭模式可取消註解
    return webdriver.Chrome(service=service, options=options)

def fetch_product_details(url):
    """
    與主程式相同: 進入商品頁面後，抓取 (name, price, offer, date, image_url)。
    若缺失 name 或 price 就返回 None。
    新增部分：透過點擊英文按鈕切換至英文頁面抓取英文商品名稱，
    結構中新增 product_eng_name 欄位。
    """
    print(f"🔵 [RETRY] 開始擷取商品資訊: {url}")
    capture_date = datetime.now().strftime("%d/%m/%Y")
    product_data = {
        "url": url,
        "name": None,
        "price": None,
        "offer": "(無特別促銷)",
        "date": capture_date,
        "image_url": None,
        "product_eng_name": "(尚未取得英文名稱)"
    }
    driver = init_driver()
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.productName")))
        # 商品名稱 + 單位
        try:
            name_elem = driver.find_element(By.CSS_SELECTOR, "div.productName")
            product_data["name"] = name_elem.text.strip()
            try:
                unit_elem = driver.find_element(By.CSS_SELECTOR, "div.productUnit")
                product_unit = unit_elem.text.strip()
                product_data["name"] += f" {product_unit}"
            except Exception:
                pass
        except Exception as e:
            print(f"⚠️ [RETRY] 無法獲取商品名稱或單位: {e}")
        # 價格
        try:
            price_elem = driver.find_element(By.CSS_SELECTOR, "span.currentPrice")
            product_data["price"] = price_elem.text.strip()
        except Exception as e:
            print(f"⚠️ [RETRY] 無法獲取價格: {e}")
        # 多件優惠
        try:
            multi_buy_elem = driver.find_element(By.CSS_SELECTOR, "div.multi-buy-count")
            product_data["offer"] = multi_buy_elem.text.strip()
        except Exception as e:
            print(f"⚠️ [RETRY] 無法獲取多件優惠: {e}")
        # 免費贈品
        try:
            free_gift_elem = driver.find_element(By.CSS_SELECTOR, "div.free-gift-title")
            free_gift_text = free_gift_elem.text.strip()
            if product_data["offer"] != "(無特別促銷)":
                product_data["offer"] += f" + 贈品：{free_gift_text}"
            else:
                product_data["offer"] = f"贈品：{free_gift_text}"
        except Exception as e:
            print(f"⚠️ [RETRY] 無法獲取免費贈品: {e}")
        # 主圖
        try:
            large_img_elem = driver.find_element(
                By.CSS_SELECTOR, 
                "swiper.largePhoto .swiper-slide-active img"
            )
            product_data["image_url"] = large_img_elem.get_attribute("src")
        except Exception as e:
            print(f"⚠️ [RETRY] 無法獲取主圖: {e}")
    except Exception as e:
        print(f"❌ [RETRY] 抓取商品資訊時發生錯誤: {e}")
    finally:
        # 如果必須欄位缺失則提前退出
        if not product_data["name"] or not product_data["price"]:
            driver.quit()
            return None

        # -------------------------------
        # 新增部分：點擊英文按鈕切換至英文頁面並取得英文商品名稱
        print(f"[INFO] 準備切換至英文頁面：{url}")
        try:
            print("[INFO] 嘗試尋找英文切換連結 (僅依據 href)...")
            # 使用 XPath 根據 href 包含 '/en/' 的連結
            eng_button = driver.find_element(By.XPATH, "//a[contains(@href, '/en/')]")
            print("[INFO] 找到英文切換連結，點擊切換...")
            eng_button.click()
            # 等待英文頁面載入（假設英文頁面仍使用 div.productName 顯示商品名稱）
            wait = WebDriverWait(driver, 25)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.productName")))
            eng_name_elem = driver.find_element(By.CSS_SELECTOR, "div.productName")
            eng_name = eng_name_elem.text.strip()
            if eng_name:
                print(f"[INFO] 英文商品名稱取得: {eng_name}")
            else:
                print("[WARN] 英文商品名稱為空")
            product_data["product_eng_name"] = eng_name
        except Exception as e:
            print(f"[DEBUG] 切換英文頁面失敗: {url}, 錯誤: {e}")
            product_data["product_eng_name"] = "(無法擷取英文名稱)"
        driver.quit()

    if not product_data["name"] or not product_data["price"]:
        return None
    return product_data

def main():
    # 1) 讀取 fail_products.json
    try:
        with open("fail_products.json", "r", encoding="utf-8") as f:
            fail_list = json.load(f)
    except Exception as e:
        print(f"❌ 無法讀取 fail_products.json，請先確認檔案是否存在且格式正確。錯誤: {e}")
        return

    if not fail_list:
        print("✅ 沒有任何失敗連結需要重試。")
        return

    print(f"🔁 準備重試 {len(fail_list)} 筆失敗連結...")

    # 2) 讀取 combined_products_pns.json
    try:
        with open("combined_products_pns.json", "r", encoding="utf-8") as f:
            combined_data = json.load(f)
    except Exception as e:
        print(f"❌ 無法讀取 combined_products_pns.json，請確認檔案是否存在且格式正確。錯誤: {e}")
        return

    products_list = combined_data.get("products", [])
    # 轉成 dict 方便更新 (key: url)
    product_dict = {}
    for item in products_list:
        url = item["url"]
        product_dict[url] = item
        # 如果沒有 uid，則加入 uid
        if "uid" not in product_dict[url]:
            product_dict[url]["uid"] = hashlib.md5(url.encode("utf-8")).hexdigest()

    # 3) 用多執行緒重試
    still_fail = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_item = {
            executor.submit(fetch_product_details, item["url"]): item 
            for item in fail_list
        }
        for future in concurrent.futures.as_completed(future_to_item):
            fail_item = future_to_item[future]
            url = fail_item["url"]
            data = future.result()
            if data:
                print(f"✅ [RETRY] 成功擷取: {url}")
                new_record = {
                    "name": data["name"],
                    "price": data["price"],
                    "offer": data["offer"],
                    "date": data["date"],
                    "image_url": data["image_url"],
                    "product_eng_name": data["product_eng_name"]
                }
                # 如果該 URL 不在 product_dict 中，則新建
                if url not in product_dict:
                    product_dict[url] = {
                        "url": url,
                        "main_category": fail_item.get("main_category", []),
                        "sub_categories": fail_item.get("sub_categories", []),
                        "history": [],
                        "uid": hashlib.md5(url.encode("utf-8")).hexdigest()  # 生成 uid
                    }
                # 合併 main_category 與 sub_categories
                for cat in fail_item.get("main_category", []):
                    if "main_category" in product_dict[url] and cat not in product_dict[url]["main_category"]:
                        product_dict[url]["main_category"].append(cat)
                for subcat in fail_item.get("sub_categories", []):
                    if "sub_categories" in product_dict[url] and subcat not in product_dict[url]["sub_categories"]:
                        product_dict[url]["sub_categories"].append(subcat)
                # 加入新的 history 紀錄
                product_dict[url]["history"].append(new_record)
                # 更新最新欄位
                product_dict[url]["name"] = data["name"]
                product_dict[url]["price"] = data["price"]
                product_dict[url]["offer"] = data["offer"]
                product_dict[url]["date"] = data["date"]
                product_dict[url]["image_url"] = data["image_url"]
                product_dict[url]["product_eng_name"] = data["product_eng_name"]
            else:
                print(f"❌ [RETRY] 仍然失敗: {url}")
                still_fail.append(fail_item)

    # 4) 更新 combined_data 的 products 與 update_date
    updated_products = list(product_dict.values())
    combined_data["products"] = updated_products
    combined_data["update_date"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # 5) 寫回 combined_products_pns_with_eng.json
    try:
        with open("combined_products_pns_with_eng.json", "w", encoding="utf-8") as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"❌ 寫入 combined_products_pns_with_eng.json 失敗: {e}")

    # 6) 寫回新的 fail_products.json (仍失敗的商品)
    try:
        with open("fail_products.json", "w", encoding="utf-8") as f:
            json.dump(still_fail, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"❌ 寫入 fail_products.json 失敗: {e}")

    print(f"\n✅ 重試結束，成功修復 {len(fail_list) - len(still_fail)} 筆，仍失敗 {len(still_fail)} 筆。")

if __name__ == "__main__":
    main()