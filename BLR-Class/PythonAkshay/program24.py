# print the series of values from 0 to n if you found value which is a multiple of 17 and 3 then break itand display the value
i=1
while True:
    if i%3==0 and i%17==0:
        break
    i+=1
print(i)