#if elif else statement>>>>>>ticket prices for different age groups
# show ticket pricing 
#1 to 3 free
# 4 to 10 150
# 11 to 60  250
# above 60 200
# age = input("please inter your age")
# if int(age) == 0 or int(age)< 0 :
#     print("you cannot watch")
# elif 0 < int(age) <= 3:
#     print("enjoy free")
# elif 3 <int(age) <= 10:
#     print("pay 150")
# elif 10 <int(age) <= 60:
#     print("pay 250")
# else:
#     print("pay 200") 
age= input("please enter your age")
if int(age)<= 3:
    print("enjoy free")
elif 3 < int(age) <15:
    print("pay 100")
elif 15 < int(age)<40:
    print("pay 500")
elif 40 < int(age)<60:
    print("pay 250")
else:
    print("pay 50")


    