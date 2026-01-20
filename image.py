import sys
sys.stdout.reconfigure(encoding='utf-8')

import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.utils import requote_uri

# Set your chromedriver path
driver_path = "/opt/homebrew/bin/chromedriver"
service = Service(driver_path)
options = webdriver.ChromeOptions()
# Uncomment the following line to run headless:
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Product detail URL (replace with your test URL)
product_url = "https://www.wellcome.com.hk/zh-hant/p/Meadows%20Home軟抽面紙(細)%205PK/i/101838602.html"
# Use requote_uri to ensure proper encoding for headers
safe_product_url = requote_uri(product_url)
driver.get(safe_product_url)

# Wait for the image element to appear
wait = WebDriverWait(driver, 10)
try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.preview-wrapper div.small img")))
except Exception as e:
    print("找不到圖片元素:", e)
    driver.quit()
    exit(1)

# Get the image URL
img_elem = driver.find_element(By.CSS_SELECTOR, "div.preview-wrapper div.small img")
img_url = img_elem.get_attribute("src")
print("取得圖片 URL:", img_url)
driver.quit()

# Set headers, using the safe_product_url as Referer
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
    ),
    "Referer": safe_product_url
}

try:
    # Using verify=False to bypass SSL verification (if needed)
    resp = requests.get(img_url, headers=headers, timeout=10, verify=False)
    if resp.status_code == 200:
        image_filename = "downloaded_image.jpg"  # or generate filename dynamically
        with open(image_filename, "wb") as f:
            f.write(resp.content)
        print(f"圖片已下載，檔名：{image_filename}")
    else:
        print("圖片下載失敗，狀態碼:", resp.status_code)
except Exception as e:
    print("下載圖片時發生錯誤:", repr(e))