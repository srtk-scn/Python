#alphabet or not

char=input("enter the character")
# if (char>='a' and char<='z') or (char>='A' and char<='Z'):
#     print('ALPHABET')
# else:
#     print('not a alphabet')


# def isalpha(char):
#     if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
#         return 'ALPHABET'
#     return 'not a alphabet'
# print(isalpha(char))



def isalpha(char):
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')
print(isalpha(char))