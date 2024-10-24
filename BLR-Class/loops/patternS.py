# #print the NO by nested list 
# str1= "NO"
# print_N=[[' ' for i in range(6)] for j in range(6)]
# print_O=[[' ' for i in range(6)] for j in range(6)]


# #code for N
# for row in range(6):
#     for col in range(6):
#         if col==0 or col==5 or (row==col and (col!=0 and col!=5)):
#             print_N[row][col]='*'
    

# #code for O

# for row in range(6):
#     for col in range(6):
#         if (col==0 or col==5) and (row!=0 and row!=5) or (row==0 or row==5) and (col!=0 and col!=5):
#             print_O[row][col]='*'
#         #     print('*',end='')
#         # else: 
#         #     print(end=' ')
#     # print()

#code for S
for row in range(7):
    for col in range(4):
        if row==0 or row==3 or row==6 or (col==0 and row<3) or (col==6 and row>3):
            print('*',end=' ')
        else:
            print(' ',end='') 
    print()

#code for A
























# for i in range(6):
#     for j in range(6):
#         print(print_N[i][j],end='')
#     print(end='  ')
#     for J in range(6):
#         print(print_O[i][j],end='')
#     print()
    