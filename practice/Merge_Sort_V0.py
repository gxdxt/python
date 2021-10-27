# merge sort

# 나눌 수 없을 때까지 데이터를 자른다.

# 나눈 데이터를 병합한다.

# 총 2개의 함수를 생성해야 한다.
import random

def split(list):
    if len(list) <= 1:
        return list
    medium = int(len(list)/2)
    left = split(list[:medium])
    right = split(list[medium:])
    return merge(left, right)

def merge(left, right):
    merged = list()
    lp, rp = 0, 0

    # 3 cases
    # 1. left / right 남아있을 때
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        else:
            merged.append(left[lp])
            lp += 1

    # 2. left만 남아있을 때
    while len(left) > lp:
        merged.append(left[lp])
        lp += 1


    # 3. right만 남아있을 때
    while len(right) > rp:
        merged.append(right[rp])
        rp += 1

    return merged

data_list = random.sample(range(50), 10)
print(data_list)
print(split(data_list))
