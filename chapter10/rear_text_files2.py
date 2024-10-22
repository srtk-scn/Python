#read file
#open function
# read method
# seek method>>to change the position of cuursor
#tell method>> to know where is our curser
#readline method>>read only one line
# readlines method>> gives the list
#close method
# f=open('zxc.txt','r')
# print(f.tell())
# print(f.read())
# print(f'current curser position{f.tell()}')
# print('BEFORE SEEK METHOD')
# f.seek(0)
# print('after seek method')
# # print(f.read())         #this will no reprint the text file data because in fist read curser is at the end of the file.fron there nothing to read
# print(f'current curser position{f.tell()}')
# print(f.read())
# f.close()

# print(f.readline(),end='')
# print(f.readline())
# print(f.readline())

f=open('zxc.txt','r')         # to open a file not in thr same folder we have to give path to that file raw string is used to avoid escape sequrnce
lines=f.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line,end='')
print(f.closed)
f.close()
print(f.closed)
#
# print(f.name)                       #to print the name of the text file
# print(f.closed)

# for line in f:                       #we can iterate f object also
#     print(line,end="")
# for l in f.readlines()[:2]:
#     print(l)
# f.close()