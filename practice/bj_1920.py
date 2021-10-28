def binary(list, data):
    if len(list) <= 1:
        if list[0] == data:
            return 1
        else:
            return 0

    medium = len(list) // 2
    if list[medium] < data:
        binary(list[medium:], data)
    else:
        binary(list[:medium], data)


def binary_teacher(data, start, end):
    if start > end:
        return False

    median = (start + end) // 2
    if N_list[median] > data:
        return binary_teacher(data, start, median-1)
    elif N_list[median] < data:
        return binary_teacher(data, median+1, end)
    else:
        return True

for item in M_list:
    if binary_teacher(item, 0, N-1):
        print(1)
    else:
        print(0)
