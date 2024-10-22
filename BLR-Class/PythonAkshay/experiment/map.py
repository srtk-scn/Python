a=[1,2,3,4,5]
z=list(map(lambda v: v**2,a))
print(z)

b=[1,2,3,4,5,6]
j=list(map(lambda x,y: x+y,a,b))
print(j)