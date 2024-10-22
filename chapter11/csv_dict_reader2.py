# from csv import DictReader
# with open('file.csv','r') as rf:
#     csv_reader=DictReader(rf)
#     # print(csv_reader)                         #address
#     for row in csv_reader:
#         print(row)
#         print(row['name'])



from csv import DictReader
with open('F:\new python course\chapter11\file1.csv','r') as rf:
    csv_reader=DictReader(rf,delimiter='|')
    # print(csv_reader)                         #address
    for row in csv_reader:
        print(row)
        print(row['name'])