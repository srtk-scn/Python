n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i<=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()   
print("-"*50)
n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()   
print("-"*50)
print("-"*50)
n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i==j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()   
print("-"*50)
n=5
for j in range(1,n+1):
    for i in range(1,n+1):
        print(i,end=" ")
    print()   
print("-"*50)
