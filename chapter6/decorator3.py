
from functools import wraps
def outer_func(func):
    @wraps(func)
    def inner_func(*args,**kwargs):
        '''this is inner function doc string'''
        print('this is awesome func')
        return func(*args,**kwargs)
    return inner_func

@outer_func
def add(a,b):
    '''add doc string'''
    return a+b
print(add(5,7))
print(add.__name__)
print(add.__doc__)
