# write a program to check whether the string contains only alphabets or not

def isalpha(s):
    for i in s:
        if not (i>='a' and i<='z' or i>='A' and i<='Z'):
            return False
    return True
if isalpha("salgsdfjgkjk"):
    print("only alphabets")
else:
    print("not only alphabets")