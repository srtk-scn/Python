#check whethwe the given number is a perfect fibbonacci number or not
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)

# print(fibo(5))
def is_fibo(num):
    n=1
    while True:
        if fibo(n)>num:
            return False
        if fibo(n)== num:
            return True
        n+=1
print(is_fibo(0))
print(is_fibo(35))