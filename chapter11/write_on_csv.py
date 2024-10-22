# writer ,DictWriter
#
# from csv import writer
# with open('file3.csv','w') as wf:
#     csv_writer=writer(wf)
#     # methods ---writerow, writerows
#     # csv_writer.writerow(['name','coountry'])
#     # csv_writer.writerow(['sarthak', 'india'])
#     # csv_writer.writerow(['golu', 'pakistan'])
#     csv_writer.writerows([['name','coountry'],['sarthak', 'india'],['golu', 'pakistan']])



from csv import writer
with open('file3.csv','w',newline='') as wf:
    csv_writer=writer(wf)
    #methods ---writerow, writerows
    csv_writer.writerow(['name','coountry'])
    csv_writer.writerow(['sarthak', 'india'])
    csv_writer.writerow(['golu', 'pakistan'])