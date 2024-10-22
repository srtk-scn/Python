import xlrd
workbook=xlrd.workbook("objects.xlsx")
worksheet=workbook.sheet_by_name('BasePage')
print(worksheet)
print(workbook)