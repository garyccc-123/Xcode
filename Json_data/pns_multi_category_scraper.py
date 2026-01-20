import time
import json
import concurrent.futures
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib

# 請改為你系統安裝的 chromedriver 路徑
CHROMEDRIVER_PATH = "/opt/homebrew/bin/chromedriver"

def init_driver():
    """初始化 Chrome 瀏覽器 (可選擇 headless 模式)"""
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    # 如需無頭模式 (headless) 請解除下列註解：
    # options.add_argument("--headless")
    return webdriver.Chrome(service=service, options=options)

def scrape_product_links(subcategory_url):
    """
    從指定的小分類頁面抓取所有商品連結 (以 set 去重)，並回傳 list
    """
    print(f"🔵 開始抓取子分類頁面商品連結: {subcategory_url}")
    driver = init_driver()
    product_links = set()
    try:
        driver.get(subcategory_url)
        time.sleep(5)  # 初次載入時間較長
        print("🔄 開始滾動頁面以加載所有商品...")
        prev_item_count = 0
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(6)
            product_tiles = driver.find_elements(By.TAG_NAME, "pns-product-tile")
            new_item_count = len(product_tiles)
            print(f"  🔹 當前頁面商品數量: {new_item_count}")
            if new_item_count == prev_item_count:
                print("  🟡 商品數量沒有變化，停止滾動")
                break
            prev_item_count = new_item_count
        for tile in product_tiles:
            try:
                a_tag = tile.find_element(By.TAG_NAME, "a")
                href = a_tag.get_attribute("href")
                if href:
                    product_links.add(href)
            except Exception as e:
                print(f"⚠️ 無法擷取某個商品連結: {e}")
        print(f"✅ 成功找到 {len(product_links)} 個商品連結")
    except Exception as e:
        print("❌ 擷取子分類頁面商品連結發生錯誤:", e)
    finally:
        driver.quit()
    return list(product_links)

def fetch_product_details(url):
    """
    進入商品頁面後，抓取商品資訊：
      - 商品名稱 + 單位（div.productName, div.productUnit）
      - 商品價格（span.currentPrice）
      - 多件優惠（div.multi-buy-count）
      - 免費贈品（div.free-gift-title）
      - 圖片網址（示範抓取第一張大圖，可自行擴充）
    並透過點擊英文按鈕切換至英文頁面抓取英文商品名稱，
    結構中新增 product_eng_name 欄位。
    """
    print(f"🔵 開始擷取商品資訊: {url}")
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

        # (1) 商品名稱 + 單位（中文版）
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
            print(f"[DEBUG] 取得中文名稱失敗: {url}, {e}")

        # (2) 價格
        try:
            price_elem = driver.find_element(By.CSS_SELECTOR, "span.currentPrice")
            product_data["price"] = price_elem.text.strip()
        except Exception as e:
            print(f"[DEBUG] 取得價格失敗: {url}, {e}")

        # (3) 多件優惠
        try:
            multi_buy_elem = driver.find_element(By.CSS_SELECTOR, "div.multi-buy-count")
            product_data["offer"] = multi_buy_elem.text.strip()
        except Exception:
            pass

        # (4) 免費贈品
        try:
            free_gift_elem = driver.find_element(By.CSS_SELECTOR, "div.free-gift-title")
            free_gift_text = free_gift_elem.text.strip()
            if product_data["offer"] != "(無特別促銷)":
                product_data["offer"] += f" + 贈品：{free_gift_text}"
            else:
                product_data["offer"] = f"贈品：{free_gift_text}"
        except Exception:
            pass

        # (5) 圖片
        try:
            large_img_elem = driver.find_element(By.CSS_SELECTOR, "swiper.largePhoto .swiper-slide-active img")
            product_data["image_url"] = large_img_elem.get_attribute("src")
        except Exception as e:
            print(f"[DEBUG] 取得圖片失敗: {url}, {e}")

        # 檢查必須欄位
        if not product_data["name"] or not product_data["price"]:
            print(f"[棄掉] 必須欄位缺失: {url}")
            return None

        # -------------------------------
        # 新增部分：點擊英文按鈕切換至英文頁面並取得英文商品名稱
        print(f"[INFO] 準備切換至英文頁面：{url}")
        try:
            print("[INFO] 嘗試尋找英文切換連結 (contains(text(),'English'))...")
            eng_button = driver.find_element(By.XPATH, "//a[contains(@href, '/en/')]")
            print("[INFO] 找到英文切換連結，點擊切換...")
            eng_button.click()
            # 等待英文頁面載入（假設英文頁面仍使用 div.productName）
            wait = WebDriverWait(driver, 25)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.productName")))
            eng_name_elem = driver.find_element(By.CSS_SELECTOR, "div.productName")
            eng_name = eng_name_elem.text.strip()
            if eng_name:
                print(f"[INFO] 英文商品名稱取得: {eng_name}")
            else:
                print(f"[WARN] 英文商品名稱為空")
            product_data["product_eng_name"] = eng_name
        except Exception as e:
            print(f"[DEBUG] 切換英文頁面失敗: {url}, 錯誤: {e}")
            product_data["product_eng_name"] = "(無法擷取英文名稱)"
    except Exception as e:
        print(f"❌ 抓取商品資訊時發生錯誤: {e}")
    finally:
        driver.quit()

    return product_data

def main():
    """
    以下將你提供的所有「大分類」→「子分類」與對應網址，整合成多層結構，
    並依序抓取各層級分類商品連結與商品資訊。
    """
    # 每個大分類對應一個子分類字典
    categories = {
 
    "水果/蔬菜": {
        "水果": [
            "https://www.pns.hk/zh-hk/食品及飲品/水果/c/04090100",
        ],
        "蔬菜": [
            "https://www.pns.hk/zh-hk/食品及飲品/蔬菜/c/04090200"
        ]
    },

 
    "飲品": {
        "汽水": [
            "https://www.pns.hk/zh-hk/食品及飲品/汽水/c/04010200"
        ],
        "即飲茶類、咖啡、奶茶": [
            "https://www.pns.hk/zh-hk/食品及飲品/即飲茶類、咖啡、奶茶/c/04010300"
        ],
        "奶類、乳酪飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/奶類、乳酪飲品/c/04010400"
        ],
        "植物奶、大豆飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/植物奶、大豆飲品/c/04010500"
        ],
        "沖調飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/咖啡、沖調飲品、熱飲/c/04010600"
        ],
        "果汁": [
            "https://www.pns.hk/zh-hk/食品及飲品/果汁、椰子水/c/04010700"
        ],
        "運動及能量飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/運動及能量飲品/c/04010800"
        ],
        "涼茶": [
            "https://www.pns.hk/zh-hk/食品及飲品/涼茶、草本飲品/c/04010901"
        ],
        "原箱飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/原箱飲品/c/04011000"
        ]
    },

 
    "酒精飲品": {
        "啤酒": [
            "https://www.pns.hk/zh-hk/啤酒/c/04012004"
        ],
        "蘋果酒、果酒、雞尾酒": [
            "https://www.pns.hk/zh-hk/蘋果酒、果酒、雞尾酒/c/04012007"
        ],
        "紅酒": [
            "https://www.pns.hk/zh-hk/紅酒/c/04012001"
        ],
        "白酒": [
            "https://www.pns.hk/zh-hk/白酒/c/04012019"
        ],
        "香檳、有氣酒": [
            "https://www.pns.hk/zh-hk/香檳、有氣酒/c/04012002"
        ],
        "氈酒、甜酒": [
            "https://www.pns.hk/zh-hk/其他烈酒、氈酒、甜酒/c/04012010"
        ],
        "白蘭地、干邑": [
            "https://www.pns.hk/zh-hk/白蘭地、干邑/c/04012008"
        ],
        "清酒、燒酒、果味米酒": [
            "https://www.pns.hk/zh-hk/清酒、吟釀、燒酌、泡盛、果味米酒/c/04012015"
        ],
        "無酒精酒": [
            "https://www.pns.hk/zh-hk/無酒精酒/c/04012018"
        ]
    },


    "糧油": {
        "米": [
            "https://www.pns.hk/zh-hk/食品及飲品/米/c/04040100"
        ],
        "即食粉麵/飯": [
            "https://www.pns.hk/zh-hk/食品及飲品/即食麵-飯、粉麵、意大利粉/c/04040200"
        ],
        "油": [
            "https://www.pns.hk/zh-hk/食品及飲品/油/c/04040300"
        ],
        "麵粉、烘焙用料、梳打粉": [
            "https://www.pns.hk/zh-hk/食品及飲品/麵粉、烘焙用料、梳打粉/c/04040400"
        ]
    },

    "零食": {
        "餅乾、曲奇": [
            "https://www.pns.hk/zh-hk/食品及飲品/餅乾、曲奇/c/04070200",
            "https://www.pns.hk/zh-hk/食品及飲品/日韓零食/c/04070100"
        ],
        "薯片、蝦片、爆谷": [
            "https://www.pns.hk/zh-hk/食品及飲品/薯片、蝦片、爆谷/c/04070300"
        ],
        "朱古力、糖果、香口膠": [
            "https://www.pns.hk/zh-hk/食品及飲品/朱古力、糖果、香口膠/c/04070400"
        ],
        "果乾、果仁、紫菜": [
            "https://www.pns.hk/zh-hk/食品及飲品/果乾、果仁、紫菜/c/04070600"
        ],
        "魚肉腸、肉乾": [
            "https://www.pns.hk/zh-hk/食品及飲品/即食雞胸、魚肉腸、肉乾/c/04070700"
        ],
        "蛋卷、糕點": [
            "https://www.pns.hk/zh-hk/食品及飲品/蛋卷、糕點、鳳梨酥/c/04070800"
        ],
        "布丁、啫喱、糖水": [
            "https://www.pns.hk/zh-hk/食品及飲品/布丁、啫喱、糖水/c/04070900"
        ]
    },

  
    "調味料、醬料": {
        "鹽、糖、其他調味料": [
            "https://www.pns.hk/zh-hk/食品及飲品/鹽、糖、其他調味料/c/04060100"
        ],
        "豉油": [
            "https://www.pns.hk/zh-hk/食品及飲品/豉油、生抽/c/04060200"
        ],
        "醬料": [
            "https://www.pns.hk/zh-hk/食品及飲品/醬料/c/04060300",
            "https://www.pns.hk/zh-hk/食品及飲品/日韓醬料/c/04060400"
        ]
    },


    "罐頭": {
        "罐頭肉": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭肉、午餐肉/c/04050101"
        ],
        "罐頭海鮮": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭魚、海鮮/c/04050102"
        ],
        "罐頭鮑魚": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭鮑魚/c/04050103"
        ],
        "罐頭水果": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭水果/c/04050104"
        ],
        "罐頭湯": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭湯/c/04050105"
        ],
        "罐頭蔬菜、豆": [
            "https://www.pns.hk/zh-hk/食品及飲品/罐頭蔬菜、豆/c/04050106"
        ]
    },

    "早餐、果醬": {
        "麵包糕點": [
            "https://www.pns.hk/zh-hk/食品及飲品/麵包糕點/c/04110100"
        ],
        "燕麥、穀類": [
            "https://www.pns.hk/zh-hk/食品及飲品/燕麥、穀類早餐/c/04110200"
        ],
        "果醬": [
            "https://www.pns.hk/zh-hk/食品及飲品/果醬、蜜糖、三文治醬/c/04110300"
        ]
    },


    "冷凍食品(乳製品,豆製品,蛋類)": {
        "蛋類": [
            "https://www.pns.hk/zh-hk/食品及飲品/蛋類/c/04081030"
        ],
        "豆製品": [
            "https://www.pns.hk/zh-hk/食品及飲品/豆腐、豆製品/c/04081060"
        ],
        "乳製品": [
            "https://www.pns.hk/zh-hk/食品及飲品/乳製品/c/04081000"
        ],
        "冷凍飲品": [
            "https://www.pns.hk/zh-hk/食品及飲品/冷凍飲品/c/04081040"
        ]
    },


    "急凍食品": {
        "急凍海鮮": [
            "https://www.pns.hk/zh-hk/食品及飲品/冷凍、急凍海鮮/c/04080100"
        ],
        "急凍肉類": [
            "https://www.pns.hk/zh-hk/食品及飲品/冷凍、急凍肉類/c/04080200"
        ],
        "丸類、冷盤": [
            "https://www.pns.hk/zh-hk/食品及飲品/丸類、冷盤美食/c/04080500"
        ],
        "餃子、雲吞": [
            "https://www.pns.hk/zh-hk/食品及飲品/餃子、雲吞/c/04080600"
        ],
        "點心、湯丸": [
            "https://www.pns.hk/zh-hk/食品及飲品/點心、湯丸/c/04080700"
        ],
        "薄餅、急凍小食": [
            "https://www.pns.hk/zh-hk/食品及飲品/薄餅、急凍小食/c/04080900"
        ],
        "急凍麵食、年糕": [
            "https://www.pns.hk/zh-hk/食品及飲品/急凍麵食、年糕/c/04081010"
        ]
    },

  
    "肉類": {
        "牛肉": [
            "https://www.pns.hk/zh-hk/食品及飲品/牛肉/c/04080301"
        ],
        "豬肉": [
            "https://www.pns.hk/zh-hk/食品及飲品/豬肉/c/04080302"
        ],
        "家禽": [
            "https://www.pns.hk/zh-hk/食品及飲品/家禽/c/04080303"
        ]
    },


    "個人護理": {
        "牙膏": [
            "https://www.pns.hk/zh-hk/個人護理、健康/牙膏/c/07040100"
        ],
        "漱口水": [
            "https://www.pns.hk/zh-hk/個人護理、健康/漱口水/c/07040500"
        ],
        "沐浴露": [
            "https://www.pns.hk/zh-hk/個人護理、健康/沐浴露/c/07020100"
        ],
        "防曬用品": [
            "https://www.pns.hk/zh-hk/個人護理、健康/防曬用品/c/07020500"
        ],
        "止汗、香體用品": [
            "https://www.pns.hk/zh-hk/個人護理、健康/止汗、香體、-爽身粉/c/07020400"
        ],
        "潤膚產品": [
            "https://www.pns.hk/zh-hk/個人護理、健康/潤膚產品/c/07020300"
        ],
        "洗髮水": [
            "https://www.pns.hk/zh-hk/個人護理、健康/洗髮水/c/07030100"
        ],
        "護髮素": [
            "https://www.pns.hk/zh-hk/個人護理、健康/護髮素/c/07030200"
        ],
        "修護、焗油、精華": [
            "https://www.pns.hk/zh-hk/個人護理、健康/修護、焗油、精華/c/07030300"
        ],
        "染髮產品": [
            "https://www.pns.hk/zh-hk/個人護理、健康/染髮產品/c/07030400"
        ],
        "洗手液": [
            "https://www.pns.hk/zh-hk/個人護理、健康/洗手液/c/07050100"
        ]
    },

    "女士衛生護理": {
        "衛生巾、護墊": [
            "https://www.pns.hk/zh-hk/個人護理、健康/衛生巾、護墊/c/07060100",
            "https://www.pns.hk/zh-hk/個人護理、健康/衛生棉條、月經杯/c/07060200"
        ],
        "除毛用品": [
            "https://www.pns.hk/zh-hk/個人護理、健康/除毛用品/c/07060300"
        ],
        "女士衛生潔膚液": [
            "https://www.pns.hk/zh-hk/個人護理、健康/女士衛生潔膚液/c/07060400"
        ]
    },


    "剃鬚用品": {
        "剃鬚刀": [
            "https://www.pns.hk/zh-hk/個人護理、健康/剃鬚刀/c/07070100"
        ],
        "補充刀片": [
            "https://www.pns.hk/zh-hk/個人護理、健康/補充刀片/c/07070200"
        ],
        "剃鬚膏、泡沫、啫喱": [
            "https://www.pns.hk/zh-hk/個人護理、健康/剃鬚膏、泡沫、啫喱/c/07070300"
        ]
    },

  
    "紙巾": {
        "廁紙、卷紙": [
            "https://www.pns.hk/zh-hk/家居生活/廁紙、卷紙/c/05010100"
        ],
        "盒裝紙巾、抹手紙": [
            "https://www.pns.hk/zh-hk/家居生活/盒裝-軟抽紙巾、抹手紙/c/05010200"
        ],
        "廚房紙": [
            "https://www.pns.hk/zh-hk/家居生活/廚房紙/c/05010300"
        ],
        "紙手巾": [
            "https://www.pns.hk/zh-hk/家居生活/迷你紙手巾/c/05010400"
        ],
        "清潔濕紙巾": [
            "https://www.pns.hk/zh-hk/家居生活/清潔濕紙巾/c/05010500"
        ],
        "濕紙巾及濕廁紙": [
            "https://www.pns.hk/zh-hk/家居生活/個人護理濕紙巾及濕廁紙/c/05010600"
        ]
    },


    "家居清潔": {
        "漂白水、清潔劑": [
            "https://www.pns.hk/zh-hk/家居生活/漂白水、清潔劑/c/05020100"
        ],
        "清潔工具": [
            "https://www.pns.hk/zh-hk/家居生活/清潔工具/c/05020200"
        ],
        "抽濕用品": [
            "https://www.pns.hk/zh-hk/家居生活/抽濕用品/c/05020401"
        ]
    },


    "廚房清潔": {
        "百潔綿布、海綿": [
            "https://www.pns.hk/zh-hk/家居生活/百潔綿布、海綿/c/05030100"
        ],
        "洗潔精": [
            "https://www.pns.hk/zh-hk/家居生活/洗潔精/c/05030200"
        ],
        "廚房清潔劑": [
            "https://www.pns.hk/zh-hk/家居生活/廚房清潔劑/c/05030300"
        ]
    },

   
    "浴室清潔": {
        "潔廁劑": [
            "https://www.pns.hk/zh-hk/家居生活/潔廁劑/c/05040100"
        ],
        "浴室清潔劑": [
            "https://www.pns.hk/zh-hk/家居生活/浴室清潔劑/c/05040200"
        ],
        "通渠用品": [
            "https://www.pns.hk/zh-hk/家居生活/通渠用品/c/05040400"
        ]
    },

 
    "洗衣用品": {
        "洗衣液": [
            "https://www.pns.hk/zh-hk/家居生活/洗衣液/c/05050101"
        ],
        "洗衣粉": [
            "https://www.pns.hk/zh-hk/家居生活/洗衣粉/c/05050102"
        ],
        "洗衣珠、洗衣紙": [
            "https://www.pns.hk/zh-hk/家居生活/洗衣珠、洗衣紙/c/05050103"
        ],
        "柔順劑": [
            "https://www.pns.hk/zh-hk/家居生活/柔順劑/c/05050104"
        ],
        "衣物消毒": [
            "https://www.pns.hk/zh-hk/家居生活/衣物消毒/c/05050105"
        ],
        "衣物清香、除菌噴霧": [
            "https://www.pns.hk/zh-hk/家居生活/衣物清香、除菌噴霧/c/05050106"
        ],
        "去漬、漂白": [
            "https://www.pns.hk/zh-hk/家居生活/去漬、漂白/c/05050107"
        ]
    },

    
    "廚房用品": {
        "食物儲存、保鮮紙": [
            "https://www.pns.hk/zh-hk/家居生活/食物儲存、保鮮紙/c/05060100"
        ],
        "垃圾袋": [
            "https://www.pns.hk/zh-hk/家居生活/垃圾袋/c/05060200"
        ]
    }
}

    

    merged_products = {}
    all_links_collected = []

    # 1) 大分類 → 子分類 → 各網址
    for main_cat, sub_cat_dict in categories.items():
        for sub_cat_name, url_list in sub_cat_dict.items():
            for sub_url in url_list:
                print(f"\n==== 抓取：[{main_cat}] - [{sub_cat_name}] | 子網址: {sub_url}")
                links = scrape_product_links(sub_url)
                for link in links:
                    if link not in merged_products:
                        merged_products[link] = {
                            "url": link,
                            "main_category": [],
                            "sub_categories": [],
                            "history": []
                        }
                    if main_cat not in merged_products[link]["main_category"]:
                        merged_products[link]["main_category"].append(main_cat)
                    if sub_cat_name not in merged_products[link]["sub_categories"]:
                        merged_products[link]["sub_categories"].append(sub_cat_name)
                all_links_collected.extend(links)

    all_links = list(set(all_links_collected))
    print(f"\n✅ 總共獲取到 {len(all_links)} 個商品連結")

    # 2) 並行擷取商品詳細
    fail_products = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(fetch_product_details, link): link for link in all_links}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            data = future.result()
            if data:
                new_record = {
                    "name": data["name"],
                    "price": data["price"],
                    "offer": data["offer"],
                    "date": data["date"],
                    "image_url": data["image_url"],
                    "product_eng_name": data["product_eng_name"]
                }
                merged_products[url]["history"].append(new_record)
                merged_products[url]["name"] = data["name"]
                merged_products[url]["price"] = data["price"]
                merged_products[url]["offer"] = data["offer"]
                merged_products[url]["date"] = data["date"]
                merged_products[url]["image_url"] = data["image_url"]
                merged_products[url]["product_eng_name"] = data["product_eng_name"]
            else:
                fail_products.append({
                    "url": url,
                    "main_category": merged_products[url]["main_category"],
                    "sub_categories": merged_products[url]["sub_categories"],
                    "uid": hashlib.md5(url.encode("utf-8")).hexdigest()
                })

    for product in merged_products.values():
        product["uid"] = hashlib.md5(product["url"].encode("utf-8")).hexdigest()

    output_data = {
        "update_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "products": list(merged_products.values())
    }

    with open("combined_products_pns_with_eng.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    with open("fail_products.json", "w", encoding="utf-8") as f:
        json.dump(fail_products, f, ensure_ascii=False, indent=4)

    print(f"\n✅ 成功擷取 {len(all_links) - len(fail_products)} 筆商品")
    print(f"❌ 無法擷取 {len(fail_products)} 筆商品，請檢查 `fail_products.json`")

if __name__ == "__main__":
    main()