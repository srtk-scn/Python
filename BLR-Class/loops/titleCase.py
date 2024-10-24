# WAP to check whether a given string in title case or not

def is_title(s):
    for i in range(len(s)):
        if (i==0 or s[i-1]==' ') and \
                s[i]>='a' and s[i]<='z':
            return False
        elif (i!=0 and s[i-1]!=" ") and \
                s[i]>='A' and s[i]<='Z':
            return False
    return True

print(is_title("Hello G$%^  "))

#write a program to convert the given string in title case
def make_title(s):
    flag=""
    for i in range(len(s)):
        if i==0 and s[i]>='a' and s[i]<='z':
            flag+=chr(ord(s[i])-32)
        elif (i!=0 and s[i-1]==" ") and s[i]>='a' and s[i]<='z':
            flag+=chr(ord(s[i])-32)
        elif (i!=0 and s[i-1]!=" ") and s[i]>='A' and s[i]<='Z':
            flag+= chr(ord(s[i])+32)
        else :
            flag+=s[i]
    return flag

print(make_title("sHHJ sJKHJK SljkhL DDDK"))