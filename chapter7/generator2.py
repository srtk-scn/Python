#create

def num(n):
    for i in range(1,n+1):
        print("before yeild statement")
        yield i
        print("after yeild statement")

k=num(10)                       #only one time executable
print(k)
print(next(k))
print(next(k))



# for i in k:
# # 
#     print(i)
# for i in k:
#     print(i)
