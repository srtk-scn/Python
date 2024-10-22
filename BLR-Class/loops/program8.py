# index of the sub string present in a string
def index(sub,s,start=0,end=0):
    if end==0 or end>len(s):
        end=len(s)
    c=0
    for i in range(0, len(s)):
        if s[i] == sub[0] and i + len(sub) <= end:
            if s[i:i + len(sub)] == sub:
                return i
print(index('ll','hello world'))

