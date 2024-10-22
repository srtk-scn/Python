from csv import DictReader
with open('pycsv.py', 'r') as rf:
    csv_reader=DictReader(rf,delimiter='|')
    # print(csv_reader)                         #address
    for row in csv_reader:
        print(row)
        print(row['name'])