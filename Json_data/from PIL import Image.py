from PIL import Image
import pytesseract
import re

img = Image.open("/Users/gary/Desktop/debug_sell_022543.png")  # 換成你的圖檔名

# 建議用這個 config，辨識一行數字
custom_config = r'--psm 7 -c tessedit_char_whitelist=0123456789.,'

text = pytesseract.image_to_string(img, config=custom_config)
print("OCR辨識原文：", text)

# 用正則式找第一個有小數點的數字（如23,415.02或23415.02）
match = re.search(r'[\d,]+\.\d+', text)
if match:
    price = float(match.group(0).replace(',', ''))
    print("轉成數字：", price)
else:
    print("找不到數字")