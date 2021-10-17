import random

def bubble(data):

    for index in range(len(data) - 1):
        swap = False
        # 어차피 한 턴 마다 그 턴에 가장 큰 수는 맨 뒤로 위치하기 때문에 하나씩 범위를 줄여 나간다!
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        # swap이 단 한 번도 이뤄지지 않았으면 그냥 종료!!
        if swap == False:
            break;

    return data

data_list = random.sample(range(100), 50)
print(data_list)
bubble(data_list)
print(data_list)
