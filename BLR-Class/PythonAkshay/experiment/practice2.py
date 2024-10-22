# def sample(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print(type(args))
#     print(type(kwargs))
#     print(*args)
#     print(*kwargs)

# sample(1,23,4,5,8,6,2,5,'hai')
# sample(a=2,b=3)
# sample(1,2,3,4,5,6,a=1,b=2,c=3)
# def sample(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# a={'a':1,'b':2,'c':3}
# sample(*a)
# def sample(n):
#     print(n,end=' ')
#     if n==0:
#         print(n,end=' ')
#         return
#     sample(n-1)
#     print(n,end=' ')
# sample(9)
# print()
# print("_"*30)
# def sample(n):
#     print(n,end=' ')
#     if n==1:
#         return
#     sample(n-1)
#     print(n-1,end=' ')
# sample(3)
# print(9)
# def rec(n):
#     if n==1:
#         return 1
#     return n*rec(n-1)
# print(rec(1))
# def fact(n):
#     f=1
#     if n==1:
#         print(n)
#     for i in range(n,0,-1):
#         f*=i
#     print(f)
# fact(5)
# def sample(n):
#     print(n)
#     # print(n)
#     # print(n)
#     if n==1:
#         return
#     sample(n-1)
#     # print()
# sample(3)
def sample(n):
    if n==0:
        return
    for i in range(n):
        print(n)

    sample(n-1)
sample(5)
    