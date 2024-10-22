p,q,r,s,t= input("enter five numbers in comma sepration").split(",")
a= int(p)
b= int(q)
c= int(r)
d= int(s)
e= int(t)


if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest") 
    else:
        if c>d:
            if c>e:
                print("c is greatest")
            else:
                print("e is greatest")
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")
else:
    if b>c:
        if b>d:
            if b>e:
                print("b is greatest")
            else:
                print("e is greatest") 
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")
    else:
        if c>d:
            if c>e:
                print("c is greatest") 
            else:
                print("e is geatest") 
        else:
            if d>e:
                print("d is greatest")
            else:
                print("e is greatest")

