class inputError(Exception):
    pass
print("Signup")
a=dict()
userid=int(input("How many id's want to create : "))
for i in range(0,userid):
    un=input("Enter an username : ")
    flag=0
    if((un.count('@')==1 and un.endswith('.com')) or (un.isdigit() and len(un)==10)):
        flag=1
    else:
        raise inputError('Enter proper username')
    pwd=input("Enter a password : ")
    upper, lower, number, special = 0, 0, 0, 0
    if len(pwd)<5 or len(pwd)>15:
        raise inputError('Enter within the limit')
    for i in pwd: 
        if i>='A' and i<='Z': 
            upper += 1
        elif i>='a' and i<='z': 
            lower += 1
        elif i>='0' and i<='9': 
            number += 1
        else:
            special += 1
    if upper>0  and number>0 and lower>0 and special>0 and flag==1:
        a[un]=pwd
    else:
        raise inputError('Enter proper password')
print("Login")
key=input("Enter username : ")
val=input("Enter password : ")
b=dict()
b[key]=val
if((key,val) in a.items()):
    print("Login Successfully")
else:
    print("Wrong username or password")
    raise inputError("Password Mismatch")