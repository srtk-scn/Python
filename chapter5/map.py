3# map function
numbers=[1,2,3,4,5,6,7,8,9]


# def square(a):
#     s=[]
#     for i in a:
#         s.append(i**2)
#     return s
# print(square(numbers))
# def squares(b):
#     return b**2
# squ= list(map(squares,numbers))
# print(squ)
# s=list(map(lambda a:a**2,numbers))
# print(s)
print(list(map(lambda a : a**2,numbers)))
# # list comp
# squnew=[i**2 for i in numbers]
# print((squnew))
d={'abc','abcd','abcde'}
# g=map(len,d)
# for i in g:
#     print(i)
print(list(map(lambda a: len(a), d)))