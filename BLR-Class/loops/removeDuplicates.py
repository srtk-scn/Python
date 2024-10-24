# wap to to print string with no duplicate
s=input('enter a string')
non_dup=""
dup=''
s.lower()
for i in s:
    if i not in non_dup:
        non_dup+=i
    elif i not in dup:
        dup+=i
print(non_dup)
print(dup)
