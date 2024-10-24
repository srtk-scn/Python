#palindrome




k=input('enter a string')
def is_pali(a):
    j=-1
    for i in range(0,len(a)//2):
        if a[i]!=a[j]:
            return False
        j=j-1
        return True
print(is_pali(k))