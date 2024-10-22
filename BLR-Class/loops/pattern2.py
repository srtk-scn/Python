#right half upper diamond by alpha
# n=int(input('enter the number of rows : '))
# for i in range(0,n):
#     if i<26:
#         print((chr(65+i)+' ')*(i+1),end=" ")
#     else:
#         break
#     print()

# lower right diamond by stars
# n=int(input('enter the number of rows : '))
# for i in range(0,n):
#     print('* '*(n-i))



#right half upper dimond by numbers
# n=int(input('enter the number of rows : '))
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

#right half upper dimond by selected numbers
# n,o=input('enter the  start and the end number of row : ').split(',')
# for i in range(int(n),(int(o)+1)):
#     for j in range(int(n),i+1):
#         print(j,end='')
#     print()

#upper half diamond numbers
# n=int(input('enter the number of rows : '))
# for i in range(n):
#     print((' ')*(n-i-1)+(str(i+1)+' ')*(i+1))


#upper half diamond reverse alpha1
# n=int(input('enter the number of rows : '))
# for i in range(n):
#     print(' '*(n-1-i)+ (chr(65+n-1+i)+' ')*(i+1))


#upper half diamond reverse alpha
# n=int(input('enter the number of rows : '))
# for i in range(n):
#     print(' '*(n-1-i),end=' ')
#     for j in range(i+1):
#         print((chr(64+n-j)+' '), end='')
#     print() 


#right diamond alpha
# n=int(input('enter the number of rows : '))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=' ')
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(chr(65+j),end=' ')
#     print()

#bottom half diamond
# n=int(input('enter the number of rows : '))
# for row in range(0,n):
#     print(' '*row,end='')
#     for col in range(n-row):#
#         print(chr(65+col)+' ', end='')
#     print()


#diamond shape stars
# n=int(input('enter the number of rows : '))
# for row in range(0,n):
#     print(" "*(n-row-1),end='')
#     for col in range(row+1):
#         print('*'+' ',end='')
#     print()
# for row in range(0,n-1):
#     print(" "*(row+1),end='')
#     for col in range(n-1-row):
#         print('*'+' ',end='')
#     print()


#upper half hollow diamond
# n=int(input('enter the number of rows : '))#5
# for row in range(n):#0,1,2,3,4
#     if row==0:
#         print(' '*(n-row-1),'*')
#     else:
#         print(' '*(n-row-1),'*'+" "*row+' '*(row-1)+ '*')


# #lower half hollow diamond 
# n=int(input('enter the number of rows : '))
# for row in range(n):
#     print("  "*row,'* ',end='')
#     if row!=n-1:
#         print('  '*(2*n-2*row-3)+'*',end='')
#     print()
        

# #lower half hollow diamond with ascending alphabets 
# n=int(input('enter the number of rows : '))
# for row in range(n):
#     print("  "*row,chr(65+row)+' ',end='')
#     if row!=n-1:
#         print('  '*(2*n-2*row-3)+chr(65+row),end='')
#     print()

#left half dimond with the help of numbers puzzle
# n=int(input('enter the number of rows : '))
# for row in range(n):
#     print(' '*(n-1-row),end='')
#     for j in range(row+1):
#         print(j+1,end='')
#     print()
# for row in range(n-1):
#     print(' '*(row+1),end='')
#     for i in range(n-1-row):
#         print(i+1,end='')
#     print()


n=int(input('enter the number of rows : '))
for row in range(n):
    print('  '*(n-1-row),end='')
    for j in range(row+1):
        print(str(j+1)+' ',end='')
    print()
for row in range(n-1):
    print('  '*(row+1),end='')
    for i in range(n-1-row):
        print(str(i+1)+' ',end='')
    print()
