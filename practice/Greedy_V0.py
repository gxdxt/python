# 항상 그 순간 순간의 최선을 선택하는 것이기 때문에 최종적으로 최선이 아닐 가능성도 있다.

def greedy_coin(value, coin_list):
    total_coin_count = 0
    pay = list()
    coin_list.sort(reverse=True)

    for item in coin_list:
        quantity = value // item
        total_coin_count += quantity
        value -= item * quantity
        pay.append([item, quantity])

    return total_coin_count, pay

coin_list = [10, 50, 100, 500, 1000, 5000]
print(greedy_coin(52510, coin_list))



