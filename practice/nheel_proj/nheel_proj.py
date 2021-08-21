import requests
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/vp/products/86224761?itemId=271802745&vendorItemId=3657804369&sourceType=srp_product_ads&clickEventId=23216e90-c4e7-4b5f-9cac-fcf74ce013ab&korePlacement=15&koreSubPlacement=1&q=%EC%83%A4%EB%B0%94%EC%8A%A4&itemsCount=36&searchId=ccd540a4610044b3b49704aebcfbf4f0&rank=0&isAddedCart='
print("play")
# response가 안될 때가 있고, 될 때가 있다. 그 이유 분석 필요
# User-Agent에 대한 정보를 넣고있지 않아서야
# 그럼 User-Agent가 어떠한 의미가 있는데??
try:
    headers = { "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" }
    response = requests.get(url, headers = headers)
except requests.exceptions.Timeout as errd:
    print("Timeout error : ", errd)
except requests.exceptions.ConnectionError as errd:
    print("Connection error : ", errd)
except requests.exceptions.HTTPError as errd:
    print("HTTP error : ", errd)
except requests.exceptions.RequestException as errd:
    print("Exception : ", errd)
print("response passed")


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-sale-price > span.total-price > strong')
    print(title.get_text())
else :
    print(response.status_code)