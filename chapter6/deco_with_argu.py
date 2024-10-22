from functools import wraps
def only_datatype_allow(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if all([type(i)==datatype for i in args]):
                return func(*args,**kwargs)
            else:
                return "other than mentioned datatype"
        return wrapper
    return decorator
@only_datatype_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string+=i
    return string
print(string_join('sarthak','sachan','jhsfbvsdj',6))