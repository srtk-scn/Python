# write a program to convert a string from lower case to upper case
a= "hey How ARE you"
result=""
for i in a:
    if i>"a" and i<"z":
        result += chr(ord(i)-32)
    else:
        result+=i
print(result)