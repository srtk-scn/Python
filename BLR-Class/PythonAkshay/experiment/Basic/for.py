# i=0
# while True:
#     print("sarthak"
# sum=0
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     sum+=i
# print(sum)
# for i in "sarthak":
#     print(i)
# n=input("enter a numner")
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)
a= input("enter a sring")
temp=""
for i in a:
    if i not in temp:
        print(f"number of occurence of {i} is {a.count(i)}")
        temp+=i
# a= input("enter a sring")
# temp=""
# for i in range(0,len(a)):
#     if a[i] not in temp:
#         print(f"number of occurence of {a[i]} is {a.count(a[i])}")
#         temp+=a[i]
