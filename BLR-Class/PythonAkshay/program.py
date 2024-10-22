a= 8
b=6
c=7
d=15
e=9


if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e) 
    else:
        if c>d:
            if c>e:
                print(c)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
else:
    if b>c:
        if b>d:
            if b>e:
                print(b)
            else:
                print(e) 
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c) 
            else:
                print(e) 
        else:
            if d>e:
                print(d)
            else:
                print(e)
