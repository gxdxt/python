import random

# 데이터가 2개일 때

# 데이터가 3개일 때


def bubble(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True
        if swap == False:
            break;
    return data

data_list = random.sample(range(100), 50)
print(data_list)
bubble(data_list)
print(data_list)
