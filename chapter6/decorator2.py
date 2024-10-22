#with arguments

def decorator_func(func):
    def wrapper_func(*a,**k):
        print('this is awesome function')
        func(*a,**k)
        print(wrapper_func)
    return wrapper_func

@decorator_func
def func1(*args,**kwargs):
    print(f'this is function 1 with arguments {args} {kwargs}')
func1(5,6,7,8,9,a=1,b=4)


@decorator_func
def add(a,b):
    return a+b