#reader,DictReader
#writer,DictWriter
from csv import DictWriter,DictReader
with open('final.csv','r') as rf:
    with open('finalz.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age':age
            })