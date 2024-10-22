class MyExecption(Exception):
    pass

def is_even(number):
    if isinstance(number,float):
        raise MyExecption('Number cannot be a Float')
    if not isinstance(number,int):
        raise TypeError("Number must be an Integer")
    return number%2==0

def is_palindrome(string):
    return string==string[::-1]
def is_string(s):
    if not isinstance(s,str):
        raise ValueError("enter string for validation")
    if isinstance(s,str):
        raise MyExecption("correctly enterned")