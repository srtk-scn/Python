d= input("enter a string")
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
# def palin(z):
#     if z==z[::-1]:
#         return "palindrome"
#     return "not a palindrome"
# print(f"{a} is {palin(a)}")
def is_palindrome(a):
    return a==a[::-1]
print(is_palindrome(d))
print(is_palindrome("naman"))
print(is_palindrome("sachan"))
