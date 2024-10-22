# a,b=10,20
# def outer():
#     x=12
#     y=11
#     print(x,y)
#     print(a,b)
#     def inner():
#         global a,b
#         a=22
#         b=33
#         print(x,y)
#         print(a,b)
#     inner()
#     print(a,b)
# print(p,q)
# outer()

# a,b=10,20
# def outer():
#     nonlocal a,b
#     a,b=b,a
#     x,y=44,55
#     def inner():
#         nonlocal x,y
#         x,y=y,x
#         print(x,y)
#     print(x,y)
#     inner()
#     print(x,y)
# outer()
# print(a,b)

# a,b=10,20
# def outer():
#     x,y=22,66
#     print(a,b)
#     def inner():
#         nonlocal x,y
#         x,y=y,x
#         print(x,y)
#     print(a,b)
#     inner()
# outer()
# print(a,b)

