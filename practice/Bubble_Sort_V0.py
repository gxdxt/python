import random

# 데이터가 2개일 때 버블정렬?
# 2개의 크기를 비교한다.
# 0번째 데이터가 1번째 데이터보다 클 경우 -> 순서 변경
# 0번째 데이터가 1번째 데이터보다 작을 경우 -> 그대로


# 데이터가 3개일 때 버블정렬?

# 데이터가 4개일 때 버블정렬?

# 먼저 전체적으로 리스트의 len만큼 훑는 for문을 돌린다.


def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break;


data_list = random.sample(range(100), 50)
print(data_list)
bubble_sort(data_list)
print(data_list)

# Time complexity


