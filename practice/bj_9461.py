def padovan(num):
    padovan = [0] * 101
    padovan[1] = 1
    padovan[2] = 1
    padovan[3] = 1
    padovan[4] = 2
    padovan[5] = 2
    padovan[6] = 3
    padovan[7] = 4
    padovan[8] = 5
    padovan[9] = 7
    padovan[10] = 9

    for index in range(11, 101):
        padovan[index] = padovan[index-2] + padovan[index-3]
    return padovan[num]

print(padovan(12))