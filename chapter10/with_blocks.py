#popular syntax to read files

#old
# f=open('text_file2.txt')
# print(f.read())
# f.close()


#popular
#with blocks
#context manager
with open('text_file2.txt') as f:
    data=f.read()
    print(data)
print(f.closed)