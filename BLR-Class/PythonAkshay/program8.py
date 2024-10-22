#write aprogram tofind the greatest of the five number
p,q,r,s,t= input("Enter five numbers in comma sepration").split(",")
a=int(p)
b=int(q)
c=int(r)
d=int(s)
e=int(t)
if a>b and a>c and a>d and a>e:
    print("a is greatest")
elif b>c and b>d and b>e:
    print("b is greatest")
elif c>d and c>e:
    print("c is greatest")
elif d>e:
    print("d is greatest")
else:
    print("e is greatest")