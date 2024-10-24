#sum from 1 to 10 number
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)
# print("-"*50)
#sum from 1 to n number
# i=1
# sum=0
# j=int(input("enter the n'th number"))
# while i<=j:
#     sum +=i
#     i+=1
# print("sum of first n natural no is:", sum)
# print("-"*50)
# input 125441 and print(1+2+5+4+4+1)
sum=0
i=0
j=input("enter a digit more than ones digit:")
while i<len(j):
    sum+=int(j[i])
    i+=1
print(sum)
# print(j[i])