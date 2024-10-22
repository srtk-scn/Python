from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return function(*args,**kwargs)
        return 'invalid dataype'
        # list = []
        # for i in args:
        #     list.append(type(i)==int)
        # if all(list):
        #     return function(*args,**kwargs)
        # else:
        #     return 'not only integers'
    return wrapper

@only_int_allow
def add(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add(1,2,3,6,5,4,7,8,9,[1,2,3,4,5]))