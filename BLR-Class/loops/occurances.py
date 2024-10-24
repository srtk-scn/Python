#count the nuumber of occurences of a chracter in a collection

# s='abcd'
# count=0
# key=input('enter the string')
# for i in s:
#     if key==i:
#         count+=1
# print(count)

def count(k,s,start,end):
    if end==0 or end>len(s):
        end=len(s)
    c=0
    for i in range(start,end):
        if s[i]==k:
            c+=1
    return c
print(count('l','hello wolrd',3,10))