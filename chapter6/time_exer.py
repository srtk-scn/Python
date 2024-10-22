import time
from functools import wraps
def decorator(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        print(f"executing .... {function.__name__}")
        t1=time.time()
        var=function(*args,**kwargs)
        t2=time.time()
        calc_time=t2-t1
        print(f"total time taken by this function{calc_time}")
        return var
    return wrapper_func
@decorator
def squares(n):
    return [i**2 for i in range(1,n+1)]
print(squares(100))

