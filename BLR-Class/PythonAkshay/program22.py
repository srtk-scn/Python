#break after getting a certain element
s= "elephant"
x='t'
i=0
while i< len(s):
    if s[i]==x:
        break
    i+=1
if i<len(s):
    print("element found", i)
else:
    print("element not found")