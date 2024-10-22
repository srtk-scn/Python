#program to describe the relation
a,b = input("enter two numbers in comma sepration").split(",")
c= int(a)
d= int(b)
if c>d:
    print("a is greater than b")
elif d>c:
    print("a is less than b")
else:
    print("a is equals to b")