# make flexible functions
# *args
# def total(a,b):
#     return a+b
# print(total(2,8))
#
# def alltotal(*args):
#     print(args)
#     print(*args)
#     print(type(args))
#     # print(type(*args))
#     tot=0
#     for i in args:
#         tot+=i
#     return tot
# print(alltotal(8,2,5,4,7,8))
#
def altotal(*args):
    # print(num)
    print(args)
    print(type(args))
    tot=0
    for i in args:
        tot+=i
    return tot
# print(altotal())

def multiply_nums(*args):
    print(args)
    print(type(args))
    multiply=1
    for i in args:
        multiply*=i
    return multiply
nums=[2,3,5]
print(*nums)
print(multiply_nums(*nums))    #unpacking from list