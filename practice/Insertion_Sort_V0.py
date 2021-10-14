import random

def Insertion_Sort(data):
    for stand in range(len(data) - 1):
        for index in range(stand + 1, 0, -1):
            if data[index] < data[index - 1]:
                data[index], data[index - 1] = data[index - 1], data[index]
            else:
                break;

data_list = random.sample(range(100), 50)
print(data_list)
Insertion_Sort(data_list)
print(data_list)