a,b=10,20
def sample():
    global a,b
    a,b=b,a
    print(a,b)
print(a,b)
sample()
print(a,b)
# a,b=10,20
# def outer():
#     global a,b
#     print(a,b)
#     a,b=b,a
#     def inner():
#         global a,b
#         print(a,b)
#         a+=10
#         b-=5
#     inner()
#     print(b,a)
# print(a,b)
# outer()
# print(b,a)
# a,b=10,20
# def outer():
#     global a,b
#     print(a,b)
#     a,b=b,a
#     def inner():
#         global a,b
#         print(a,b)
#         a+=10
#         b-=5
#         def in_inner():
#             global a,b
#             a,b=b,a
#             a*=2
#             b**=2
#         print(a,b)
#         in_inner()
#         print(b,a)
#     inner()
#     print(a,b)
# outer()
# print(a,b)
