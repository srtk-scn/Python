# hollow heart shape
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row + col==8):
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print() 

# # fill heart shape

# for i in range(4):
#     for j in range(4-i-1):
#         print(' ', end='')
#     for j in range(i+1):
#         print('* ',end='')
#     for j in range(2*(4-i-1)):
#         print(' ', end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()
# for i in range(8):
#     for j in range(i):
#         print(' ',end='')
#     for j in range(8-i):
#         print('* ',end='')
#     print()


# fill heart shape
# n=int(input('enter the number of col : '))
# s=n//2
# for i in range(s):
#     for j in range(s-i-1):
#         print(' ', end='')
#     for j in range(i+1):
#         print('* ',end='')
#     if n%2==0:
#         for j in range(2*(s-i-1)):
#             print(' ', end='')
#     else:
#         for j in range(2*(s-i-1)+1):
#             print(' ', end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()
# for i in range(n):
#     for j in range(i):
#         print(' ',end='')
#     for j in range(n-i):
#         print('* ',end='')
#     print()


# n=int(input('enter the number of col : '))
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(end=' ')
#     for j in range(i,0,-1):
#         print(j,end='')
#     for j in range(2,i+1):
#         print(j,end='')
#     print()




#code for N
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and (col>0 and col<5)):
#             print('*',end='')
#         else: 
#             print(end=' ')
#     print()

#code for O

for row in range(6):
    for col in range(6):
        if (col==0 or col==5) and (row!=0 and row!=5) or (row==0 or row==5) and (col!=0 and col!=5):
            print('*',end='')
        else: 
            print(end=' ')
    print()

