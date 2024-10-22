#write a program to add 10 to the each and every element present inside the list
a=[1,5,7,6,2,4,8,9,45]
i=0
while i<len(a):
    a[i]= a[i] + 10
    i+=1
print(a)