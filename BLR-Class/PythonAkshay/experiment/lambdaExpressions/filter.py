a=[1,2,3,4,5]
z=list(filter(lambda c: c%2==0,a))
print(z)
x=tuple(filter(lambda c: c%2==0,a))
print(x)
y=set(filter(lambda c: c%2==0,a))
print(y)
