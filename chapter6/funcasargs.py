l=[1,2,3,4,56,8,8]
def square(a):
    return a**2
# print(list(map(square,l)))
# print(list(map(lambda a:a**3 ,l)))
# #
# # print(list(map(lambda a:a**2,l)))
# #
def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list
print(my_map(square,l))
print(my_map(lambda a:a**3,l))
# def my_map2(fun,k):
#     return [fun(i) for i in k]
# print(my_map2(lambda a:a**3,l))
