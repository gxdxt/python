import random

def selection(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand + 1, len(data) - 1):
            if data[stand] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

dataList = random.sample(range(100), 50)
print(dataList)
selection(dataList)
print(dataList)