# WAP to check how may substring present in our string
s='hello world'
sub='ld'
count=0
for i in range(0,len(s)):
    if s[i]==sub[0] and i+len(sub)<=len(s):
        if s[i:i+len(sub)]==sub:
            count+=1
print(count)


def count(sub,s,start=0,end=0):
    if end==0 or end>len(s):
        end=len(s)
    c=0
    for i in range(0, len(s)):
        if s[i] == sub[0] and i + len(sub) <= end:
            if s[i:i + len(sub)] == sub:
                c += 1
    return c
print(count('ll','hello world'))