from functools import wraps
def print_function_data(func):
    # @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"you are calling {func.__name__}")
        print(func.__doc__)
        return func(*args,**kwargs)
    return wrapper
@print_function_data
def add(a,b):
    '''this function takes two aguments and returns the sum'''
    return a+b
print(add(5,7))