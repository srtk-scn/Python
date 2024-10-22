name = "   Sarthak Sachan    "
dots = ".............."
print(name)   #cannot see right side space left
# lstrip()   method
print(name + dots)           #we can see now ryt side spaces
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)   #cannot vanish space between the name
# for vaninishing spaces between the name
print(name.replace(" ", ""))
print(name.replace(" ", "") + dots)  # replace all the space either in mid front back

