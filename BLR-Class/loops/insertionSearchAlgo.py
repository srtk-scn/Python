#write a program to demonstrate insertion sorting algorithma


#insertion sort alogorithm
a=[3,1,7,2,5,4]
n=len(a)
for passno in range(1,n):
    i=passno
    while i!=0 and a[i-1]>a[i]:
        a[i],a[i-1]=a[i-1],a[i]
        i-=1
        print(a)
print(a)

def insertion_sorting(a):
    n = len(a)
    for passno in range(1, n):
        i = passno
        while i != 0 and a[i - 1] > a[i]:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a
print(insertion_sorting(a))
