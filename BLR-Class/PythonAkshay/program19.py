#write a program to check string contains only alphabets or not
a="abc123"
count=0
for i in a:
    if not (i>='a' and i<='z' or i>='A' and i<="Z"):
        count+=1
if count==0:
        print("string contains only alphabats")
else:
        print("string contains alphanumeric with special symbol")