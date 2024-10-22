# lowecase if it is in upper case 
a= "SARTHAK SACHAN"
result=""
for i in a:
    if i>="A" and i<="Z":
        result+=chr(ord(i)+32)
    else:
        result+=i
print(result)