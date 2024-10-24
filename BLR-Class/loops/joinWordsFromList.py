#write a program to join the list of string by using the specific sub string

def join(l,sub):
    res=''
    count=0
    for i in l:
        res+=i
        count+=1
        if count<len(l):
            res+=sub
    return res
print(join(['hai','how','are','you'],' '))