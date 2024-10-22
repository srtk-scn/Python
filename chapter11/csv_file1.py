from csv import reader

with open('file.csv','r') as rf:
    csv_reader=reader(rf)                          #csv reader is a iterator
    next(csv_reader)
    for row in csv_reader:
        print(row)
    # for row in csv_reader:
    #     print(row)