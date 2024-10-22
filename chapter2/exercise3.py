# name, char = input("please enter name and character seprated by comma ").split(",")
# print(len(name))
# sachan = (name + char).lower()
# print(sachan.count("s"))


#OR
# name, char = input("please enter name and character seprated by comma ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count : {name.count(char)}")   #  spaces problem from input>>>> strip method


#name.lower().count(char.lower())
# name, char = input("please enter name and character seprated by comma ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count : {name.lower().count(char.lower())}")
# #
# 
# 
#probem solution by strip method 
#    "    Sarthak     "    >>>>>>>     "Sarthak"   >>>>>>>>>  "sarthak"
#     "  H   "    >>>>>>>>>       "H"    >>>>>>>>   "h"
# # name.strip().lower().count(char.strip().lower())
# # char.strip().lower()
# name, char = input("please enter name and character seprated by comma ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count : {name.strip().lower().count(char.strip().lower())}") # problem solved


name,char=input('enter the name and character in comma spration').split(',')
# print(f"your name is {name.strip()} and number of character is{name.strip().lower().count(char.strip().lower())}")
print(f"your name is {name.replace(' ','')} and number of character is{name.replace(' ','').lower().count(char.replace(' ','').lower())}")

# name, char= input("enter your name and character by comma sepration").split(",")
# print(len(name))
# print(f"charcter count{name.strip().lower().count(char.strip().lower())}")
# print(f"character count:{name.replace(" ","").lower().count(char.replace(" ","").lower())}")
# name, char= input("please enter your name and the character in comma sepration").split(",")
# print(f"charcter count {name.strip().lower().count(char.strip().lower())}")
# print(f"charcter count {name.replace(" ","").lower().count(char.replace(" ","").lower())}")