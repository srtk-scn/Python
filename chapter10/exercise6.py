

# with open('sachan.txt','r') as rf:
#     with open('output6.txt','a') as wf:
#         for line in rf.readlines():
#             name,salary=line.split(',')
#             wf.write(f'{name}\'s salary is {salary}')
with open('file2.txt','r') as rf:
    with open("text_file3.txt" , 'a') as af:
        for line in rf.readlines():
            name,sal=line.split(',')
            af.write(f'{name}\'s salary is {sal}') 