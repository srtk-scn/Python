a="sarthak sachan@123"
b=""
for i in a:
    if i >="a" and i<="z" or i>="A" or i<="Z":     
        if i not in "aeiouAEIOU":
            b+=i
print("consonant",len(b))
        

