import random


sample = list()
sample = random.sample(range(100), 50)
# 그냥 sort >> 결과를 return하여 sample 자체가 정렬된다.
print('sort')
sample.sort()
print(sample)

# reverse sort >> 역순으로 정렬
sample.sort(reverse=True)
print('reverse sort')
print(sample)

# 그냥 sorted >> 결과를 return하지 않고 일시적으로만 정렬된 척
print('sorted')
print(sorted(sample))
print(sample)
