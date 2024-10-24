#write a program to check whether the given number is a perfect factorial or not
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
# print(factorial(5))

def is_factorial(num):
    n=1
    while True:
        if factorial(n)>num:
            return False
        if factorial(n)==num:
            return True
        n+=1
print(is_factorial(125))
