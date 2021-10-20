def func(n):
    print(n)
    if n == 1:
        return n

    elif n%2 == 0:
        n = n/2
        return func(int(n))
    else:
        n = (3*n) + 1
        return func(n)