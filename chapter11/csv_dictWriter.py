from csv import DictWriter
with open('final.csv','w',newline="") as wf:
    csv_writer=DictWriter(wf,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    #writerow, writerows
    # csv_writer.writerow({
    #     'firstname':'sarthak',
    #     'lastname': 'sachan',
    #     'age':25
    # })
    # csv_writer.writerow({
    #     'firstname': 'shashwat',
    #     'lastname': 'sachan',
    #     'age': 18
    # })
    #writerows--->[dict1,dict2,dict3]
    csv_writer.writerows([
        {'firstname':'sarthak','lastname': 'sachan','age':20},
        {'firstname':'shashwat','lastname': 'sachan','age':25},
        {'firstname':'karan','lastname': 'sachan','age':564}
    ])