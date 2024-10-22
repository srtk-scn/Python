def is_even(number):
    if isinstance(number,str):
        raise TypeError('string not allowed')
    if isinstance(number,float):
        raise ValueError('float not allowed')
    return number%2 ==0

def is_palindrome(string):
    if not isinstance(string, str):
        raise TypeError('enter only strings')
    return string==string[::-1]
