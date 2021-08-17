myString = "arsenal"

print(myString)
print(myString[0])
print(myString[-1])
print(myString[2:])
print(myString[:3]) #Up to but not including!!
print(myString[::]) #To see the all the way from the beginning to the end
#the third place is for the step size, I can decide the size of jump point
print(myString[::2])
# immutability
# 단순히 String 속에 있는 Char를 변경하는 것은 불가능은
# myString[0] = 'K' 이런 식의 방법이 불가
# 그렇기에 사용하는 방법
team = myString[1:]
print('K' + team)
