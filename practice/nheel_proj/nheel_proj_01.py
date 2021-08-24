import requests
from bs4 import BeautifulSoup

coupang_price = '1,000'

def defineHeaders(a):
    headers = {"User-Agent": a}
    return headers

def nheelProj(headers, id, url, price):
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
        try:
            title = soup.select_one('div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-sale-price > span.total-price > strong')
            print(title)
            coupang_price = title.get_text().split('원')[0]
            print('first' + coupang_price)
            if title is None:
                print('title is None')
                title2 = soup.select_one('div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-coupon-price > span.total-price > strong')
                coupang_price = title2.get_text().split('원')[0]
                print('second' + coupang_price)
            if coupang_price is None:
                coupang_price = '1,000'
                print('third' + coupang_price)
        except AttributeError as e:
            print(e)

        coupang_price = int(coupang_price.replace(',', ''))
        # print(coupang_price)
        original_price = int(price)
        # print(original_price)
        if (coupang_price > original_price) :
            flag = False
        else :
            flag = True

        if flag:
            return print(id)
        else:
            return print('id: ('+ id + ')는 쿠팡가가 너무 높습니다.')

    else:
        print(response.status_code)

#nheelProj({ "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" }, 'https://www.coupang.com/vp/products/86224761?itemId=271802745&vendorItemId=3657804369&sourceType=srp_product_ads&clickEventId=23216e90-c4e7-4b5f-9cac-fcf74ce013ab&korePlacement=15&koreSubPlacement=1&q=%EC%83%A4%EB%B0%94%EC%8A%A4&itemsCount=36&searchId=ccd540a4610044b3b49704aebcfbf4f0&rank=0&isAddedCart=', 1000)
# { "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" }
# 'https://www.coupang.com/vp/products/86224761?itemId=271802745&vendorItemId=3657804369&sourceType=srp_product_ads&clickEventId=23216e90-c4e7-4b5f-9cac-fcf74ce013ab&korePlacement=15&koreSubPlacement=1&q=%EC%83%A4%EB%B0%94%EC%8A%A4&itemsCount=36&searchId=ccd540a4610044b3b49704aebcfbf4f0&rank=0&isAddedCart='
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
if __name__ == "__main__":
    # 띄어쓰기를 쉼표로 대체해서 list로 받아와야해

    #띄어쓰기 단위로 list 안에 넣고, 줄바꿈 단위로 다른 list 생성하고
    # 리스트 완성이 되면 len(list)로 for문 돌려야해
    product_list = []
    product = []
    while True:
        product = input().split('\t')
        if product == ['exit']:
            break
        else:
            product_list.append(product)
    # 한땀 한땀 함수에 넣어서
    a = input('Headers를 입력해주세요 : ')

    for i in range(0, len(product_list)):
        nheelProj(defineHeaders(a), product_list[i][0], product_list[i][1], int(product_list[i][2].replace(',', '')))

    # 결과값 출력하면 되겠다.
    #a = input('headers: ')


    #url = input('url: ')
    #price = input('정가: ')
    #nheelProj(defineHeaders(a), url, price)