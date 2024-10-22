#program to count total number of vowel present in a string
a= "sarthak sachan"
count= 0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print(count)