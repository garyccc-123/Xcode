import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    抓取網頁 HTML 內容
    """
    headers = {
        # 模擬一般瀏覽器的 User-Agent
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("成功抓取網頁")
        return response.text
    else:
        print(f"網頁請求失敗，狀態碼：{response.status_code}")
        return None

def extract_text(html):
    """
    解析 HTML 並提取頁面中的純文字
    """
    soup = BeautifulSoup(html, "html.parser")
    # 使用空格作為分隔符，並去除多餘空白
    text = soup.get_text(separator=" ", strip=True)
    return text

if __name__ == "__main__":
    url = "https://www.wellcome.com.hk/zh-hant/category/100011/1.html"
    html = fetch_page(url)
    if html:
        page_text = extract_text(html)
        print("提取的文字內容：")
        print(page_text)