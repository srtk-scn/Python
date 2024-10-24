#check wheathr the string comtains only alphabetas or not

def isalpha(s):
    for i in s:
        if not (i >='a' and i<='z' or i >='A' and i<='Z'):
            return False
        return True
print(isalpha('hmafdnbasvfj sgcshFDFDKGD'))