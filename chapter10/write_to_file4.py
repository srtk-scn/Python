#w, a ,r
# with open('text_file2.txt','r') as f:
#     data=f.read()
#     print(data)

# with open('file2.txt','w') as f:                #overwrite the previous data  or if you give new name then the new file is created
#     f.write('hello sachan')

# with open('text_file4.txt','a') as f:
#     f.write('\nplease add my append data')

with open('text_file4.txt','r+') as f:         #do not create a file
    f.write('please do it from beggining\n')                    #write file from the beggining if there any charcter in place it will replace
    f.seek(len(f.read()))
    f.write('please add characters at the last')
    print(f.read())