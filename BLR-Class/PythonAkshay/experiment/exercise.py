a=input("enter any string")
temp=""
i=0
while i<len(a):
    if a[i] not in temp:
        print(f"number of occurance of {a[i]} is {a.count(a[i])}")
        temp+=a[i]
    i+=1
print(temp)

