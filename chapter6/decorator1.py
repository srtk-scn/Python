#decorator enhances the functionality of a function

def decorator_func(func):
    def wrapper_func():
        print('this is a awesome function')
        func()
    print(wrapper_func)
    return wrapper_func
@decorator_func
def sarthak():
    print('this is sarthak function')
 
# sarthak()


def outer(func):
    def inner(*args,**kwargs):
        print("this is inner function")
        func(*args,**kwargs)
    return inner
@outer
def sachan(*args,**kwargs):
    print(f"tuple{args} and dictionary{kwargs}")
sachan(1,2,3,4,4,5,567,78,a=1,b=3,c=5,v=78)




# # @decorator_func
# def shashwat():
#     print('this is shashwat function')
# shashwat()

# decorator_func(sarthak)
# def decorat(func):
#     def inner(args):
#         print("this is special addition by inner")
#         print(args)
#         print(func.__name__)

#         func(args)
#     inner("S")

# @decorat
# def sarthak(ar):
#     print(f"this is sarthak function with {ar}")
#     print('leaving the sarthak function')
# sarthak("Sachin")