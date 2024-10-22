import math


a=int(input("enter a number to check perfect square"))
b=math.sqrt(a)
print(b)
if a//b==b:
    print("it is a perfect square")
else:
    print('not a perfect square')


