#program to reverse a string without using slicing

def reverse(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
s=input('enter sting')
print(reverse(s))

def reverse_(s):
    r=''
    for i in range(-1,(-len(s)-1),-1):
        r+=s[i]
    return r
print(reverse_(s))


#by while loop