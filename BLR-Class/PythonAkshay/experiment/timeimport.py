import time

def timer(func):
    def inner(arguments):
        start_time=time.time()
        func(arguments)
        end_time=time.time()
        print("total time taken is", end_time-start_time)
    return inner
@timer
def cube(n):
    for i in range(1,n+1):
        res=i**3
@timer
def pow4(n):
    for i in range(1,n+1):
        res=i**4


@timer
def sqr(n):
    for i in range(1,n+1):
        res=i**2
sqr(1000)
cube(1000)
pow4(1000)
