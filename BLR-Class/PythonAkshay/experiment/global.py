a=5#global variable
def func():
    global a # for changing to global
    a=7#local variable
    return a
print(a)
print(func())
print(a)