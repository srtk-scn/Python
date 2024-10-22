class My_favorite_Exception(Exception):
    pass


def square(a):
    if isinstance(a,str):
        raise ValueError("number cannot be string")
    return a**2


def cube(b):
    if isinstance(b,str):
        raise My_favorite_Exception('nuber canot be string')
    return b**3

def fact(n):
    if n in [0,1]:
        res=1
    else:
        res=1
        for i in range(n,0,-1):
            res=res*i
    return res



