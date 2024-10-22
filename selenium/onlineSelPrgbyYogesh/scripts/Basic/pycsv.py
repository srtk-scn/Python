from csv import DictWriter
with open('final.csv','w',newline="") as wf:
    csv_writer=DictWriter(wf,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    csv_writer.writerows([
        {'firstname':'sarthak','lastname': 'sachan','age':20},
        {'firstname':'shashwat','lastname': 'sachan','age':25},
        {'firstname':'karan','lastname': 'sachan','age':564}
    ])

