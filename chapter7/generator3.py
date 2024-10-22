# def genrator_even(n):
#     # for i in range(1,n+1):
#     for i in range(2,n+1,2):
#         # if i%2==0:
#             yield i

# for num in genrator_even(15):
#     print(num)
# #
# #
square=(i**2 for i in range(1,11))
print(next(square))
for i in square:
    print(i)
cube=(i**3 for i in range(5,11))
print(next(cube))
print(next(cube))
print(next(cube))
print(next(cube))