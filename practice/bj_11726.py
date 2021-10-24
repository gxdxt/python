# nx2 타일링

# DP 알고리즘으로 풀이

# 점화식 찾기??
# 가장 작을 때부터 리스트를 작성해서, 패턴을 구하는 것이 일반적이다.
def tile(num):
    cache = [1 for index in range(num+1)]
    cache[1] = 1
    cache[2] = 2

    for index in range(3, num+1):
        cache[num] = cache[num-1] + cache[num-2]
    return cache[num]



# 빈 리스트 만들기
# 문제 자체에서 n의 값을 1 <= n <= 1,000으로 설정했기 때문에
# 빈 리스트의 크기는
dp = [0] * 1001 # 이렇게 하면 빈 리스트 생성되네,,신기방기
print(dp[1000])

# 초기값 설정
dp[1] = 1
dp[2] = 2

# 점화식 기반으로 계산값 적용하기
for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2]

# 특정 값 테스트

n = int(input())

print(dp[n]%10007)

