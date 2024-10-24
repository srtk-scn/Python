# WAP to convert the given string in upper case

def upper(s):
    re=""
    for i in s:
        if i>='a' and i<='z':
            re+=chr(ord(i)-32)
        else:
            re+=i
    return re
print(upper('asfgshnJJJJJ'))

#WAP to convert in lower case
def lower(s):
    re=""
    for i in s:
        if i>='A' and i<='Z':
            re+=chr(ord(i)+32)
        else:
            re+=i
    return re
print(lower('asfgshnJJJJJ'))