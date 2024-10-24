# 1
# k=int(input('enter the loop value in row : '))
# l=int(input('enter the loop value in column : '))
# for i in range(1,k):
#     for j in range(1,l):
#         print('*',end=' ')
#     print()


#2
# k=int(input('enter the loop value in row : '))
# for i in range(1,k+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

#3
# k=int(input('enter the number of rows: '))
# l=1
# for i in range(1,k+1):
#     for j in range(1,l+1):
#         print('*',end=' ')
#     l+=2
#     print()

# 4
# k=int(input('enter the number of rows: '))
# for i in range(0,k):
#     for j in range(1,k-i-1):
#         print(end='')
#     for j in range(0,i+1):
#         print('*',end="")
#     print()

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()
print('='*50)
for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()
print('='*50)
for i in ('A','B','C','D','E'):
    for j in range(1,6):
        print(i, end=" ")
    print()
print('='*50)
for i in range(1,6):
    for j in ('A','B','C','D','E'):
        print(j, end=" ")
    print()
print('='*50)
for i in ('A','B','C','D','E'):
    for j in range(1,6):
        print(i, end=" ")
    print()
print('='*50)
