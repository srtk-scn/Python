a=input("enter any string")
temp=""
i=0
while i<len(a):
    if a[i] not in temp:
        print(f"number of occurance of {a[i]} is {a.count(a[i])}")
        temp+=a[i]
    i+=1
print(temp)

# wap to count the number of ocurrences of a particular character in a given string between the limits
def count(key,string,start_index=0,end_index=0):
    if end_index==0:
        end_index=len(string)
    c=0
    if key in string[start_index:end_index]:
        for i in range(start_index,end_index):
            if string[i] == key:
                c+=1
        return c
    return c
print(count("k","sakkrthaksack",5))





# def count(key,string,start_index=0,end_index=0):
#     if end_index==0:
#         end_index=len(string)
#     c=0
#     if key in string[start_index:end_index]:
#         for i in string:
#             if i == key:
#                 c+=1
#         return c
#     return c
# print(count("k","sakkrthaksack",5))
