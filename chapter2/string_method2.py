#replace() method 
#find() method >>>>>>> position of word
#center method >>>>>>> for **word**

string = "she is beautifull and she is a good dancer"
print(string.replace(" ", "_"))
print(string.replace("is", "was"))
print(string.replace("is", "was", 1))
print(string.replace("is", "was", 2))
print(string.find("is"))
print(string.find("is", 5))
# # if we dont know the position of 1st is then
is_pos1 = string.find("is")  #   is_pos1   >>>>  number
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)# position of another is


# center method
name = "sarthak"     #  string length=7
#  **sarthak**        for 4 star to be print we add  7(string)+4(star)
print(name.center(11, "*"))
print(name.center(9, "*"))
print(name.center(len(name) + 6,"*"))
print(name.center(15,'%'))
print(name.center(len(name)+ 8,'$'))