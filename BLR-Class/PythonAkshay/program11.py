#program to find the GCD of two numbers
p,q= input("enter two numbers in comma sepration").split(",")
m=int(p)
n=int(q)
while(m!=0 and n!=0):
    if m>n:
        m-=n
    else:
        n-=m
if m==0:
    print(("gcd is " ,n))
else:
    print("gcd is " ,m)
        