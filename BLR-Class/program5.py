#alphanumeric or not

# char=input('enter a character :')
# while True:
#     if (char>='a' and char<='z') or (char>='A' and char<='Z')\
#             or (char>='0' and char<='9'):
#         print('alphanumeric')
#         break
#
#     else:
#         print("not an alphanumeric")
#         char = input('enter a character :')

#by ascii value_________

char=input('enter a character :')
if (ord(char) in range(ord('a'),ord('z')+1)) or ord(char) in range(ord('A'),ord('Z')+1) or  ord(char) in range(ord('0'),ord('9')+1):
    print('alphanumeric')
else:
    print('not a alphanumerc')