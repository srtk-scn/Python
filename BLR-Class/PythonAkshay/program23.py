s=[1,2,3,4,5,6,7,8,9,10]
x=11
i=0
found= False
for i in range(len(s)):
    if s[i]==x:
        found=True
        break
    i+=1
if found==True:
    print("Element found")
else:
    print("elemant not found")