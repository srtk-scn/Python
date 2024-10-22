#problem
#ask user to input a umber containing more than one digit 
#example= 1256
#calculate 1+2+5+6 and print


# num = input("enter a four digit number")
# print(f"sum of all the digits: {int(num[0])+int(num[1])+int(num[2])+int(num[3])}")


num = input("enter your number")
i = 0
total= 0 
# while i < len(num):
#     total += int(num[i])
#     i+=1
# print(total)
for i in num:
    total+=int(i)
print(total)
