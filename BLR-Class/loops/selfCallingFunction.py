#recurssion>>>>>>>>self calling functions


# import time
# def display(n):
#     if n==0:
#         return
#     print(n)
#     time.sleep(2)
#     display(n-1)
# display(5)

# def display(n):
#     print(n)
#     if n==0:
#         return
#     time.sleep(2)
#     display(n-1)
#     print(n)
# display(5)

#program to print the sum of n numbers
# n=5
# def add(n):
#     if n==0:
#         return 0
#     count=0
#     for i in range(1,n):
#         count+=i
#     return count
# print(add(5))
# sum of n natural numbers

def add(n):
    if n==0:
        return 0
    return n+add(n-1)
start=time.time()
add(900)
end=time.time()
print(end-start)
def product(n):
    if n==0 or n==1:
        return 1
    return n*product(n-1)
print(product(5))
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(10))

# WAP to find the n fabonacci numvber
#nth = (n-1)th + (n-2) th
# def fibo(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
# print(fibo(5))


# convert binaery search algorithm to recurssive format

