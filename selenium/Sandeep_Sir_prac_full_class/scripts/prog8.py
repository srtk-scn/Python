import sys
print(sys.argv)
print(sys.argv[0])
x=int(sys.argv[1])
y=int(sys.argv[2])
#
#
#
#
def add(a,b):
    print(a+b)
add(x,y)


import xlrd
workbook=xlrd.open_workbook(r'C:\Users\sarthak sachan\PycharmProjects\DemoWebShopFW\Python_Selenium_FW-master\Data\Objects.xlsx')
worksheet=workbook.sheet_by_name('HomePage')

rows=worksheet.get_rows()

print(rows)
header=next(rows)     #skipping headers
# print(next(rows))
# print(next(rows))
# print(next(rows))
# print(next(rows))
# for row in rows:
    # print(row[0])
    # print(row[2])
    # print(type(row[0]))
    # print((row[0]).value)
    # print(row[0].value,row[1].value,row[2].value)
HomePage_Objects={row[0].value:(row[1].value,row[2].value) for row in rows}   # this is he data structure we are getting in dictionary from excel sheet
print(HomePage_Objects)
print(HomePage_Objects["lnk_register"])
print(HomePage_Objects["lnk_login"])
print(HomePage_Objects["txt_search"])