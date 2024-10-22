#program to print consonent in the string
a="dogs123"
count=0
for i in a:
    if i>='a' and i<='z' or i>='A' and i<="Z":
        if i not in "aeiouAEIOU":
            count+=1
print(count)