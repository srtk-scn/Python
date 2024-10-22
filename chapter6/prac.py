# def outer(func):
#     print('control enters in outer function')
#     print('outer arguments',func) 
#     def inner(arg):
#         print('control enters in inner function')
#         print('inner argument',arg)
#         print('before task')
#         func(arg)
#         print('after task')
#         print('control leaving in inner function')
#     print('control leaves outer function')

#     return inner
#     print('control leaves outer function')


# @outer
# def sample(ar):
#     print('control in sample func')
#     print('sample arguments',ar)
#     print('control came out sample func')

# sample("sarthak")

# def trillion(a,b,/,*,key,dic):
#     print('entering billion')
#     def billion(func):
#         def million(args):
#             print(f"this is million func with{args}")
#             print(f"these are the arguments from the trillion {a},{b},{key},{dic}")
#             print(func.__name__)
#             func(args)
#         return million
#     return billion

# @trillion(1,2,key="sarthak",dic="sachan")
# def sarthak(arg):
#     print("this is under the sarthak with args", arg)
# sarthak("sachan")

def log(debug=True,msg="You called"):
    def logging(func):
        def wrapper(*args,**kwargs):
            if debug:
                print(f"{msg}{func.__name__}")
            return func(*args,**kwargs)
        return wrapper
    return logging

@log()
def add(a,b):
    return a+b
@log()
def sub(a,b):
    return a-b
print(sub(5,3))