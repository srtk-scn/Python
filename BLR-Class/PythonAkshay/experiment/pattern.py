n=5
for j in range(1,n+1):
    for i in range (1,n+1):
        print("*",end=" ")
    print()
print("-"*50)
for j in range(1,n+1):
    for i in range(1,n+1):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("-"*50)
for j in range(1,n+1):
    for i in range(1,n+1):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("-"*50)
for j in range(1,n+1):
    for i in range(1,n+1):
        if i<j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("-"*50)
for j in range(1,n+1):
    for i in range(1,n+1):
        if i>j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("-"*50)
for j in range(1,n+1):
    for i in range(1,n+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()