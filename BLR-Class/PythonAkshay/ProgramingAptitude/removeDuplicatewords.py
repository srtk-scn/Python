#write a program to have count the charecters in string and express as dictionary
#input = "aabcbda"
# output = {'a':3,'b':2,'c':1,'d':1}

# def count(ch,s):
#     cnt=0
#     for i in s:
#         if i==ch:
#             cnt+=1
#     return cnt
# # print(count('a','hgiuagaaayguiaaaaygijaa'))

# def disp(s):
#     d={}
#     for i in set(s):
#         d[i]=count(i,s)
#     return d
# print(disp('hgiuagaaayguiaaaaygijaa'))


#write a program to split the given string into list of pieces when ever we found the specified substring and 
#do as many number of splits as specifi


# def split(s,ss,sp):
#     res=['']
#     i,ires=0,0
#     while i<len(s):
#         if s[i:i+len(ss)]==ss and ires<sp:
#             res.append('')
#             ires+=1
#             i+=len(ss)
#         else:
#             res[ires]+=s[i]
#             i+=1
#     return res
# print(split('jhgjhikdfkjhkjhf','jh',5))


#write a program to join the list of strings present using specified substring
#input: ['hai', 'hello', 'world', 'how are you'] and "#"
#output: hai#hello#world#how are you

# def join(l,ch):
#     a=''
#     for i in range(len(l)-1):
#         a+=(l[i]+ch)
#     a+=l[-1]
#     return a

# print(join(['hai', 'hello', 'world', 'how are you'],'#'))


# wap to remove the duplicate words from string

def rmdup(s):
    res=''
    words=s.split(' ')
    print(words)
    for word in words:
        if word not in res:
            res+=word+' '
        else:
            res+=word+' '
    if res[-1]==' ':
        res=res[:-1]
    return res

print(rmdup("hai hello how are you who are you how his is life how bye"))
