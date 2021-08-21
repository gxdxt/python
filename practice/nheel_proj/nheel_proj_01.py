import requests
from bs4 import BeautifulSoup

def nheelProj(headers, url, price):
    print("크롤링 시작")
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.Timeout as errd:
        print("Timeout error : ", errd)
    except requests.exceptions.ConnectionError as errd:
        print("Connection error : ", errd)
    except requests.exceptions.HTTPError as errd:
        print("HTTP error : ", errd)
    except requests.exceptions.RequestException as errd:
        print("Exception : ", errd)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one(
            'div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-sale-price > span.total-price > strong')
        print(title.get_text().split('원'))
    else:
        print(response.status_code)