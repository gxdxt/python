import random

def selection(data):
    for stand in range(len(data) - 1):
        lowest = stand

        # turn의 범위가 틀렸다. stand 다음부터 select 해야한다.
        for index in range(stand+1, len(data)):
            if data[index] < data[lowest]:
                lowest = index

        data[stand], data[lowest] = data[lowest], data[stand]
    return data

data_list = random.sample(range(100), 50)
print(data_list)
selection(data_list)
print(data_list)




