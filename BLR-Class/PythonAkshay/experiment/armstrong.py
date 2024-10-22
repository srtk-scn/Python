# a=input("enter your number to check armstrong: ")
# sum=0
# for i in a:
#     sum+=(int(i))**3
# if sum==int(a):
#     print("ARMSTRONG")
# else:
#     print("NOT ARMSTRONG")
print('_'*30)
n=int(input("enter your number to check armstrong: "))
a=n
z=0
while a>0:
    b=a%10
    z+=b**3
    a=a//10
if z==n:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")



