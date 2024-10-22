#function inside function

# def outer_func():
#     def inner_func():
#         print('inside inner func')
#     return inner_func
#     print(inner_func)
# print((outer_func())())
# k=outer_func()
# k()
def outer_func2(msg):
    def inner_func2():
        print(f"this is a message{msg}")
    return inner_func2
outer_func2('april fool')()

def to_power(n):
    def number(x):
        return x**n
    return number
var=to_power(3)
print(var(5))
