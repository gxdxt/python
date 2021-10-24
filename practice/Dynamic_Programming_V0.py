# 동적 계획법
# 큰 작업을 수행하기 위해, 잘게 쪼게서 작은 작업부터 '반복'적으로 수행한 뒤의 결과값을 '기억'하여 큰 작업을 수행하는 알고리즘 기법
# Memoization(기억) 기법을 사용한다.
# 반복적으로 수행하기 때문에 재귀 함수도 사용된다.


# 대표적으로 피보나치 수열 알고리즘이 있다.

# recursive call 활용
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


## DP는 단순히 recursive와 다른 점은 >> 값을 저장하는 것!!
## 그럼 어떻게  Memoization??

def fibonacci_dp(num):
    # 저장공간 생성
    # comprehension
    cache = [0 for index in range(num+1)]
    # 이거 하면 0부터 num까지의 일정한 배열이 생성된다.
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]


