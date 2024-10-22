# def add_two(a,b): 
#     return a+b
# total=add_two(5,4)
# print(total)
# print(add_two(5,4))
# def odd_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(odd_even(6))
#or
# def odd_even(n):
#     if n%2==0:
#         return "even"
#     return "odd"
# print(odd_even(9))
# def is_even(n):
#     if n%2==0:
#         return True
#     return False
# print(is_even(8))
# def is_even(n):
#     return n%2==0
# print(is_even(9))
# def compare(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
# p=int(input("enter first number"))
# q=int(input("enter second number"))
# bigger=compare(p,q)
# print(f"{bigger} is greater")
# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# p=int(input("enter first number"))
# q=int(input("enter second number"))
# r=int(input("enter third number"))
# big= greater(p,q,r)
# print(f"{big} is greater")
def greater(a,b):
    if a>b:
        return a
    return b
p=int(input("enter first number"))
q=int(input("enter second number"))
r=int(input("enter third number"))
def greatest(a,b,c):
    # bigger= greater(p,q)
    return greater(greater(p,q),r)
# biggest= greatest(p,q,r)
print(f"{greatest(p,q,r)} is greatest")


