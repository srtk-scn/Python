
n=6
# for i in range(1,n):
#     for j in range(1,n):
#         if i<=j:
#             print('*',end=' ')
#     print()
#
# for i in range(1,n):
#     for j in range(1,n):
#         if i>=j:
#             print('*',end=' ')
#     print()
# for i in range(1,n):
#     for j in range(1,n):
#         if i>=j:
#             print(' ',end=' ')
#         else:
#             print("*", end=" ")
#     print()
# for i in range(1,n):
#     for j in range(1,n):
#         if i<j:
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()
# for i in range(1,n):
#     for j in range(1,n):
#         if i>j:
#             print(' ',end=' ')
#         elif i<j:
#             print(' ', end=' ')
#         else:
#             print('*', end=' ')
#     print()
#
# for i in range(1,n):
#     for j in range(1,n):
#         if i+j==6:
#             print('*', end=' ')
#         else:
#             print(' ',end=' ')
#     print()
for i in range(1,n):
    for j in range(1,n):
        if j>=i:
            print(' ', end=' ')
        else:
            print('*',end=' ')
    print()