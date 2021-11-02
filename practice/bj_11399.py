def shortest_greedy(num, times):
    total = 0
    total_all = 0
    times.sort()
    total_list = list()
    print(times)
    for i in range(0, num):
        total += times[i]
        total_all += total

    return total_all

people = [3, 1, 4, 3, 2]
num = 5
print(shortest_greedy(num, people))



# lecture
#for index in range(N):
#    for index2 in range(index+1):
#        total += people[index2]