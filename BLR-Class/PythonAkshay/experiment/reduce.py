import functools
# a=[1,2,3,4,5,6,8]
# def add(x,y):
#     return x+y
# print(add(5,6))

# print(functools.reduce(lambda x,y: x+y,a))
print(functools.reduce(lambda x,y: x+y,range(1,6)))