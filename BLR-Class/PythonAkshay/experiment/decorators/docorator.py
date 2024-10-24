# decorator increase the functionality of an function

# def decorator_function()

def decorator_function(any_function):
    def wrapper_function():
        print("this is awsm function")
        any_function()
    return wrapper_function
# @decorator_function


@decorator_function
def func1():
    print("this is function 1")
@decorator_function
def func2():
    print("thia is function 2")
# var=decorator_function(func1)
# var()
# func1=decorator_function(func1)
func1()
func2()


