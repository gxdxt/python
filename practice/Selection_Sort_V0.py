import random

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[index] < data[lowest]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data

data_list = random.sample(range(100), 50)
print(data_list)
selection_sort(data_list)
print(data_list)