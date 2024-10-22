#write a programto find the second largest of 4 numbers

# a,b,c,d=4,1,3,2
def great3(x,y,z):
    if x>y and x>z:
        return x
    elif y>z:
        return y
    return z
def sec_largest(a,b,c,d):
    if a>b and a>c and a>d:
        return great3(b,c,d)
    elif b>c and b>d:
        return great3(a,c,d)
    elif c>d:
        return great3(a,b,d)
    else:
        return great3(a,b,c)
print(sec_largest(2,5,3,5))
