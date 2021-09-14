hash_table = list(['O' for i in range(10)])
print(hash_table)
# list comprehension

# 간단한 hashing function
def hash_func(key):
    return key % 5

## ord(): 문자의 ASCII 코드를 출력하는 것
data1 = 'James'
data2 = 'Dave'
data3 = 'Trump'
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = data

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]