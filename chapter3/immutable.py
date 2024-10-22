#strings are immutable
string = "string"
# string[1] = 'T'
print(string.replace('t','T'))   #  string can be change by replace method by print by creating a new variable
# string.replace('t', 'T')
print(string)            # original string cannot be change so it is immutable
new_string = string.replace('t', 'T')
print(new_string)