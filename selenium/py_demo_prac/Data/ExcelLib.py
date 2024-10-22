# import xlrd
#
# def read_data(sheetname,testcase):
#     workbook=xlrd.open_workbook('TestData.xlsx')
#     worksheet=workbook.sheet_by_name(sheetname)
#     temp_data=[]
#     data=[]
#     headers=None
#     r=worksheet.get_rows()
#     for index,item in enumerate(r):
#         if not item[0].value==testcase:
#             continue
#         headers=worksheet.row_values(index-1,start_colx=2)
#         headers=",".join(item for item in headers if item)
#         break
#     r=worksheet.get_rows()
#     for item in r:
#         if item[0].value==testcase:
#             temp_data.append(tuple([temp.value for temp in item if temp.value])[1:])
#     for d in temp_data:
#         if d[0].upper()=="YES":
#             data.append(d[1:])
#     return [headers,data]
#
# print(read_data("Shopping","test_registration"))
#
#
# def read_locators(sheetname):
#     workbook=xlrd.open_workbook('Objects.xlsx')
#     worksheet=workbook.sheet_by_name(sheetname)
#     r=worksheet.get_rows()
#     next(r)
#     return {item[0].value:(item[1].value,item[2].value) for item in r}
# # print(read_locators("RegistrationPage"))



import xlrd

def read_data(worksheet,test_case):
    workbook=xlrd.open_workbook('F:\selenium\py_demo_prac\Data\TestData.xlsx')
    worksheet=workbook.sheet_by_name(worksheet)
    headers=None
    temp_data=[]
    data=[]
    r=worksheet.get_rows()
    for index,row in enumerate(r):
        if not row[0].value == test_case:
            continue
        headers=worksheet.row_values(index-1,start_colx=2)
        headers=','.join(i for i in headers if i)
        break
    print(headers)
    r= worksheet.get_rows()
    for row in r:
        if row[0].value==test_case:
            temp_data.append(tuple([temp.value for temp in row if temp.value])[1:])
    for d in temp_data:
        if d[0].upper()=='YES':
            data.append(d[1:])
    print(data)
    return [headers,data]
print(read_data('Shopping','test_login'))


def read_locaters(sheetname):
    workbook=xlrd.open_workbook('F:\selenium\py_demo_prac\Data\Objects.xlsx')
    worksheet=workbook.sheet_by_name(sheetname)
    r=worksheet.get_rows()
    next(r)
    return {row[0].value:(row[1].value,row[2].value) for row in r}

print(read_locaters('BasePage'))