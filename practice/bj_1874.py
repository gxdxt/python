def stack_array(N, num_array):
    cnt = 0
    target_num = 1
    result, target = list(), list()
    target.append(target_num)
    # 목표값이 나올 때까지, push
    while cnt < len(num_array):
        if num_array[cnt] == target[-1]:
            target.pop()
            print('-')
            cnt += 1
        else:
            target.append(target_num)
            target_num += 1
            print('+')
            continue

    return result


# 배열의 값이 나올 때까지 push를 하다가, 값이 나오면 pop
# 하지만 카운트는 올라간다.
test_array = [4, 3, 6, 8, 7, 5, 2, 1]
stack_array(8, test_array)
print('-----')
#test_array2 = [1, 2, 5, 3, 4]
#stack_array(5, test_array2)

# 연달아 빼낼 때 내림차순을 유지하는가! 가 포인트!!!


