import requests
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/vp/products/237181694?itemId=751734793&vendorItemId=4898821183&q=%EC%83%A4%EB%B0%94%EC%8A%A4&itemsCount=36&searchId=ccd540a4610044b3b49704aebcfbf4f0&rank=34&isAddedCart='
print("play")
# response가 안될 때가 있고, 될 때가 있다. 그 이유 분석 필요
response = requests.get(url)
print("response passed")


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-sale-price > span.total-price > strong')
    print(title.get_text())
else :
    print(response.status_code)