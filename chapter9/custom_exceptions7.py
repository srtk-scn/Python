#python custom exceptions
#Q-- why custom execeptions
#A-- to increase the readability of the code

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name)<8:
        # raise ValueError('name is too short')
        raise NameTooShortError('name is too short')

username=input('enter your name :')
validate(username)
print(f"Hello {username}")
