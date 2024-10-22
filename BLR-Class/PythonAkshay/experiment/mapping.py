a=[1,234,45,6,77,8,8,99,00]
# def cube(i):
#         return i**3
# a=lambda a:a**2
# print(a(20))
# print(list(map(lambda a : a**2,a)))
# print(list(map(cube,a)))

print(list(map(lambda x:True if x%2==0 else False,[1,234,45,6,77,8,8,99,00])))
f=list(filter(lambda a:a%2==0,a))
print(f)