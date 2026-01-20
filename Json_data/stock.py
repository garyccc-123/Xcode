import pyautogui
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
from PIL import Image
import pandas as pd
import time
from datetime import datetime
import re
import os

region_sell = (1346, 260, 81, 30)   # 請根據你自己的區域微調
region_buy  = (1683, 258, 93, 35)   # 請根據你自己的區域微調
desktop_path = "/Users/gary/Desktop"

records = []

def extract_price(text):
    text = text.strip().replace('\n', '')  # 去除空白和換行
    match = re.search(r'[\d,]+\.\d+', text)
    if match:
        return float(match.group(0).replace(',', ''))
    else:
        return None

print("啟動中，15秒後自動開始抓價，請把螢幕切到Plus500價格畫面...")
for i in range(15, 0, -1):
    print(f"倒數 {i} 秒...", end='\r')
    time.sleep(1)
print("開始長期自動記錄（Ctrl+C 可手動中斷）")

try:
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nowstr = datetime.now().strftime('%H%M%S')

        # 擷取圖片
        sell_img = pyautogui.screenshot(region=region_sell)
        buy_img  = pyautogui.screenshot(region=region_buy)

        # OCR 辨識（直接對原圖，參數最穩定）
        custom_config = r'--psm 7 -l eng --oem 3 -c tessedit_char_whitelist=0123456789.,'
        sell_text = pytesseract.image_to_string(sell_img, config=custom_config)
        buy_text  = pytesseract.image_to_string(buy_img,  config=custom_config)
        print("OCR辨識原文(sell):", sell_text)
        print("OCR辨識原文(buy):", buy_text)

        # 儲存前3次 debug 圖方便你檢查
        if len(records) < 3:
            sell_img.save(os.path.join(desktop_path, f"debug_sell_{nowstr}.png"))
            buy_img.save(os.path.join(desktop_path, f"debug_buy_{nowstr}.png"))

        sell_price = extract_price(sell_text)
        buy_price  = extract_price(buy_text)

        print(f"{now}: 賣出價={sell_price}  買入價={buy_price}")

        records.append({"datetime": now, "sell_price": sell_price, "buy_price": buy_price})

        # 每10筆自動存一次csv
        if len(records) % 10 == 0:
            df = pd.DataFrame(records)
            df.to_csv(os.path.join(desktop_path, "plus500_prices.csv"), index=False, encoding="utf-8-sig")
            print("自動儲存至桌面 plus500_prices.csv")

        time.sleep(60)  # 每分鐘記錄一次

except KeyboardInterrupt:
    print("手動中斷，正在儲存最後結果…")
    df = pd.DataFrame(records)
    df.to_csv(os.path.join(desktop_path, "plus500_prices.csv"), index=False, encoding="utf-8-sig")
    print("已全部儲存完畢！")