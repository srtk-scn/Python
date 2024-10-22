# to convert a string in to title case if it is not in title case
a= "dogs are bettHVJHBr than human 123"
result=""
for i in range (len(a)):
    if a[i]>="a" and a[i]<="z" or a[i]>="A" and a[i]<="Z":
        if i==0 and a[i] >="a" and a[i]<="z":
            result+= chr(ord(a[i])-32)
        elif i!=0 and a[i-1]==" " and a[i] >="a" and a[i]<="z":
            result+= chr(ord(a[i])-32)
        elif i!=0 and a[i-1]!=" " and a[i]>="A" and a[i]<="Z":
            result += chr(ord(a[i])+32)
        else:
            result += a[i]
    else:
        result += a[i]
print(result)


