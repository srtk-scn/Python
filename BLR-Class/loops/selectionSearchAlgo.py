#selection search alogothim

a=[9,3,6,2,4]
for passno in range(1,len(a)):
    min=passno-1
    for i in range(min+1,len(a)):
        if a[min]>a[i]:
            min=i
    a[passno-1],a[min]=a[min],a[passno-1]
print(a)

def selection(a):
    for passno in range(1,len(a)):
        min=passno-1
        for i in range(min+1,len(a)):
            if a[min]>a[i]:
                min=i
        a[passno-1],a[min]=a[min],a[passno-1]
    return a
print(selection([9,2,3,5,4,7,8,9,1]))

