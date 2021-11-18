
# lambda는 간소화된 함수로 생각하면 될 듯 하다.

# 기존 def 함수
def sum(a, b):
    return a + b
print(sum(24, 36))

# lambda 함수
print((lambda a, b: a+b)(24, 36))

# map 에서의 lambda 사용
# map은 인자로 '함수'와 '리스트'를 받는다.
test_list = [1, 2, 3, 4, 5]
new_test = list(map(lambda x:x**2, test_list))
print(new_test)


# reduce 에서의 lambda 사용
# reduce는 누적 집계를 사용하는 데에 사용된다.

