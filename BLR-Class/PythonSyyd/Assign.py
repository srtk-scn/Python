class myerror(Exception):
    pass
count1=0
count2=0
count3=0
count4=0
username=input("enter your username: ")
if '@' not in username and username.isdigit()==False:
    raise myerror("enter valid usename")
Password=input("enter your password: ")
if len(Password)<5 or len(Password)>16:
    raise myerror("length should be in 5 t0 15")            
for i in Password:
    if i.isdigit():
        count1+=1
    elif i.islower():
        count2+=1
    elif i.isupper():
        count3+=1
    else:
        count4+=1
if count1<1  and count2<1 and count3<1 and count4<1:
    raise myerror("paswword must have lower,upper digit and special symbol")
elif count1>=1 and count2>=1 and count3>=1 and count4>=1:
    print("Validation sucessful")