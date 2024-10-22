# # # watch coco movie if name starts with A or a and age is more than 45
# name, age = input("enter your name and enter your age in space sepration").split( )
# # # name.lower()
# if name.lower()[0] == "s" and int(age) > 45 :
# # # # if (name[0] == "s"  or name[0] == "S" ) and int(age) > 45:
#     print("you can watch coco movie")
# else:
#     print("you are tiny")


name, age = input("enter your name and age in space sepration").split( )
# if name.lower()[0] == "s" and int(age) > 55 :
if (name[0]== 's'or name[0]=='S') and int(age)>55:
    print("you can watch movie ")
else:
    print("you are young") 