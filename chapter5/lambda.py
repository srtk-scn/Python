def add(a,b):
    return a+b
print(add(4,8))
add2= lambda a,b : a+b
print(add2(4,50))
print(add2)
mul=lambda a,b : a*b
print(mul(5,8))

def is_even(a):
    return a%2==0
print(is_even(58))

even=lambda a : a%2==0
print(even(654))
last=lambda s: s[::-1]
print(last('sarthak'))

r=lambda s : len(s)>5
print(r('hga'))

# h=lambda k : True  if len(k)>5 else False
# print(h('sfafcdhg'))
f=lambda a: True if len(a)>10 else False
print(f('hgdhgchjhljh'))

f=lambda a : True if len(a)>5 else False

print(f('sarthak'))