# write a program to eliminate all the vowels present in a string
a="sarthaksachan"
result=""
for i in a:
    if i in "aeiouAEIOU":
        continue
    result+=i
print(result)