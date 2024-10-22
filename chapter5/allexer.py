# def add(*args):
#     if all([(type(arg)==int or type(arg)==float) for arg in args]):
#         total=0
#         for i in args:
#             total+=i
#         return total
#     else:
#         return "wrong input"
# print(add(2,3,5,5,6,1,8,5.5,'ghsvja'))



def add(*args):
    print(args)
    print(type(args))
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total = 0
        for i in args:
            total+=i
        return total
    else:
        return 'wrong input'
print(add(1,2,3,58,2,74.5))
