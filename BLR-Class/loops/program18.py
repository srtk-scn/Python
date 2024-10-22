#write a program to split the given string into list of words

# def split(s,key):
#     j=0
#     res=[""]
#     for i in s:
#         if i==key:
#             res.append('')
#             j+=1
#         else:
#             res[j]+=i
#     return res
# print(split('hai how are you',' '))


# def split(s,key):
#     res=['']
#     i=0
#     j=0
#     while i<len(s):
#         if s[i]==key:
#             res.append('')
#             j+=1
#         else:
#             res[j]+=s[i]
#         i+=1
#     return res
# print(split('hai how are you',' '))



def split(s,key):
    res=['']
    i=0
    j=0
    while i<len(s):
        if s[i:i+len(key)]==key:
            res.append("")
            j+=1
            i+=len(key)
        else:
            res[j]+=s[i]
            i+=1
    return res
print(split('hellohullilellolulli','ll'))
