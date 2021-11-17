# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

def print_queue(N, print_queue):
    queue = list()
    index_list = []

    # 순서를 구해야 한다.
    # 순서는 우선순위가 큰 값부터 실행하고,
    # 각각의 인덱스를 부여하고, 우선 순위대로 나열하자
    for i in range(len(print_queue)):
        index_list.append([print_queue[i], i])

    # 위에 코드를 한 줄로 줄이면
    index_list = [(i, idx) for idx, i in enumerate(print_queue)]
    print(index_list)
    count = 0 # 프린트 된 문서의 수
    while True:
        if index_list[0][0] == max(index_list, key=lambda x: x[0])[0]: # 람다를 이용해서 x[0]의 값들 중 가장 큰 값의 [0] 값을 블러온다.
            print('lambda : ' + str(max(index_list, key=lambda x:x[0])[0]))
            count += 1
            if index_list[0][1] == N:
                print(count)
                break
            else:
                index_list.pop(0)
        else:
            index_list.append(index_list.pop(0))


print(print_queue(0, [1, 1, 9, 1, 1, 1]))
print('--------')
print(print_queue(2, [1, 2, 3, 4]))
