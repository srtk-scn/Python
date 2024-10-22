#gretest of the 3 numbers
d,e,f= input("enter three numbers in comma sepration").split(",")
# a=50
# b=60
# c=8
a= int(d)
b= int(e)
c= int(f)
if a>b and a>c:
    print("a is gratest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")