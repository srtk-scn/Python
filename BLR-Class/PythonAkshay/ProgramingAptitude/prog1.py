# write a program to convert all upper case character into lowercase charcter in a string
s=input('enter a string: ')
res=""
# for i in s:
#     if 'A'<=i<='Z':
#         res+=chr(ord(i)+32)
#     else:
#         res+=i
# print(res)

# for i in range(len(s)):
#     if 'A'<=s[i]<='Z':
#         res+=chr(ord(s[i])+32)
#     else:
#         res+=s[i]
# print(res)
i=0
while i<len(s):
    if 'A'<=s[i]<='Z':
        res+=chr(ord(s[i])+32)
    else:
        res+=s[i]
    i+=1
print(res)
