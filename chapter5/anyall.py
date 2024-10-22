#if
# all[true,true,true])-------->>true


l1=[2,4,6,8,10,57]
l2=[1,3,5,7,9]

print(all([i%2==0 for i in l1]))
print(any([i%2==0 for i in l1]))

even=[]
for i in l1:
    even.append(i%2==0)
print(all(even))