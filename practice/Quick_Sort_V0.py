# 정렬 알고리즘의 꽃

# Divide and Conquer /  dc 기법 중 하나

# pivot 선택 및 정렬

# 합치기
import random

def qsort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list()
    pivot = data[0]
    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100), 100)
print(data_list)
print(qsort(data_list))

# most recent call last >> 조건 확인
# len(data) == 1 일 때만 return data하게끔 설정해놨따.
# len(data) <= 1로 변경했다.

# 더 깔끔한 방법

def qsort2(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort2(left) + [pivot] + qsort2(right)

print(data_list)
print(qsort2(data_list))

# pivot이 계속해서 가장 큰 값으로 설정될 때에는 O(n2)의 시간복잡도가 나온다.
# 일반적으로는 nlog(n)
