import tkinter

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

userAgent = ""
def getUserAgent(url):
    try:
        response = requests.get(url)
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
        print(soup)
        print('----------')
        try:
            userAgent = soup.select_one('#custom-ua-string').value
            print(userAgent)
        except AttributeError as e:
            messagebox.showinfo("오류", e)
            print(e)
    return userAgent

def defineHeaders(a):
    headers = {"User-Agent": a}
    return headers



def nheelProj(headers, id, url, price):
    try:
        response = requests.get(url, headers=userAgent)
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
            if title == None:
                title2 = soup.select_one('div.prod-price-container > div.prod-price > div.prod-price-onetime > div.prod-coupon-price > span.total-price > strong')
                coupang_price = title2.get_text().split('원')[0]
            else:
                coupang_price = title.get_text().split('원')[0]
        except AttributeError as e:
            messagebox.showinfo("오류", e)
            print(e)

        coupang_price = int(coupang_price.replace(',', ''))
        original_price = int(price)
        flag = 0
        if (coupang_price > original_price + 1000) :
            flag = 1
        if (coupang_price < original_price - 1000) :
            flag = -1


        if (flag == -1) :
            return print('id: ('+ id + ')는 현재 쿠팡가는 ('+ str(coupang_price) +')로 기존 쿠팡가 ('+ str(original_price) + ')보다 1,000원 이상 낮습니다.')
        elif (flag == 1):
            return print('id: ('+ id + ')는 현재 쿠팡가는 ('+ str(coupang_price) +')로 기존 쿠팡가 ('+ str(original_price) + ')보다 1,000원 이상 높습니다.')

        else :
            return print('id: ('+ id + ')는 이상 없습니다.')
    else:
        print(response.status_code)

if __name__ == "__main__":
    getUserAgent('https://www.whatsmyua.info/')
    print(userAgent)

    # 가장 상위 레벨의 윈도우 창 생성
    window = tkinter.Tk()

    window.title("nheel_proj_V0")
    window.geometry("640x400+100+100")

    #resize 안에 param에 0 = false , 1 = true로 지정 가능
    # (상하, 좌우)를 의미한다.
    window.resizable(False, False)

    # 입력된 값 가져오기
    def getTextInput():
        result = excelInput.get(1.0, "end")


    #위젯 이름을 사용하여 label 사용 가능
    label = tkinter.Label(window, text = "알지의 쿠팡 크롤링")
    label.pack()
    #label 끝

    #Input 시작
    excelInput = tkinter.Text(window, height=10)
    excelInput.pack()
    #Input 끝

    #Button 시작
    btnClick = tkinter.Button(window, height=1, width=10, text='click', command=getTextInput)
    btnClick.pack()
    #Button 끝
    

    # 윈도우가 종료될 때까지 창 실행
    window.mainloop()




    a = input('Headers를 입력해주세요 : ')
    product_list = []
    product = []
    while True:
        product = input().split('\t')
        if product == ['exit']:
            break
        else:
            product_list.append(product)



    for i in range(0, len(product_list)):
        nheelProj(defineHeaders(a), product_list[i][0], product_list[i][1], int(product_list[i][2].replace(',', '')))
    print("nheel proj V0 by stuoy")
    print("알지에게 도움이 되었길 바라며!")