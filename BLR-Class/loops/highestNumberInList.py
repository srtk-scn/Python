#write a program to find the largest of list of  numbers
def large(a):
    if a[0]>a[1]:
        fl=a[0]
    else:
        fl=a[1]
    for i in range(2,len(a)):
        if a[i]>fl:
            fl=a[i]
    return fl

c=[1,2,3,4,5,6,9,8,7,5,5,2,1,4,5]
print(large(c))


















#write a program to find the second largest of the list in the string
b=[1,2,3,4,58,2,3,6]
def sec_largest(a):
    if a[0]>a[1]:
        grt,sec=a[0],a[1]
    else:
        grt, sec = a[1], a[0]
    for i in range(2,len(a)):
        if a[i]>grt:
            sec,grt=grt,a[i]
        else:
            if a[i]>sec:
                sec=a[i]
    return sec
# print(sec_largest(b))
