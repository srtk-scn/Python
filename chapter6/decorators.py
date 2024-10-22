#pre decorators

def square(a):
    '''this functions takes one input and returns the square'''
    return a**2
s=square
print(square(5))
print(s(5))
print(square.__name__)
print(s.__name__)
print(square)
print(s)
print(s.__doc__)