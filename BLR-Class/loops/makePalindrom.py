#how many minimum characters that u need to add at tghe last make the string the PLINDROME

# def is_palindrom(s):
#     return s==s[::-1]
# s=input('enter the string')
# def min_char(s):
#     count=0
#     while len(s)>0:
#         if is_palindrom(s):
#             return count
#         else:
#             count+=1
#             s=s[1:]
# print(min_char(s))


#how many minimum characters that u need to add at begining make the string the PLINDROME
def is_palindrom(s):
    return s==s[::-1]
s=input('enter the string')
def min_char(s):
    count=0
    while len(s)>0:
        if is_palindrom(s):
            return count
        else:
            count+=1
            s=s[:-1]
print(min_char(s))
