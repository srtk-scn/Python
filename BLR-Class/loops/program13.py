# write a program to nth fabonacci number
# def fibbo(n):
#     fibbo1=0
#     fibbo2=1
#     for i in range(2,n):
#         fibbo=fibbo1+fibbo2
#         fibbo1,fibbo2=fibbo2,fibbo
#     return fibbo
# n=int(input('enter the nth number'))
# print(fibbo(n))

#write a program for print the list of fibbonaci series
# def fibo_series(n):
#     a=[0,1]
#     for i in range(2,n):
#         b=a[i-2]+a[i-1]
#         a.append(b)
#     return a
# print(fibo_series(n))

def fibbo(n):
    fibbo1=1
    fibbo2=2
    for i in range(2,n):
        fibbo=fibbo1*fibbo2
        fibbo1,fibbo2=fibbo2,fibbo
    return fibbo
n=int(input('enter the nth number'))
print(fibbo(n))