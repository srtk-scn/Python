# with open('file1.txt','r',encoding='utf-8') as rf:
#     print(rf.encoding)
#     data=rf.read()
#     print(data)


#to read huge amount of data by read 100 words at a time

with open('long.txt','r') as rf:
    data=rf.read(100)
    while len(data)>0:
        print(data)
        data=rf.read(100)