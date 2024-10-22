import xlrd
import os
from Library import Config


def read_data(sheetname, testcase):
    """
    Return a list with Headers as a Tuple and test data as list of Tuples:
    @parameterized_class(
                ("username", "passwrod"),
                [("foo", pwd1),("bar", pwd2)]
        )
    """
    workbook = xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    temp_data = []
    data = []
    header = None
    r = worksheet.get_rows()
    for index, item in enumerate(r):
        if not item[0].value == testcase:
            continue
        headers = worksheet.row_values(index - 1, start_colx=2)  # Read Headers
        header = tuple(headers)
        break
    r = worksheet.get_rows()  # Re-initialising iterator
    for item in r:
        if item[0].value == testcase:
            temp_data.append(tuple([temp.value for temp in item])[1:])
    for d in temp_data:
        if d[0].upper() == 'YES':
            data.append(d[1:])
    return [header, data]


def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    worksheet = workbook.sheet_by_name(sheetname)
    r = worksheet.get_rows()
    next(r)     # Skip Headers
    return {item[0].value: (item[1].value, item[2].value) for item in r}


def get_modules_to_execute():
    workbook = xlrd.open_workbook(Config.DATA_FILE_PATH)
    worksheet = workbook.sheet_by_name('Index')
    r = worksheet.get_rows()
    next(r)  # skip headers
    final = []
    for row in r:
        if row[1].value.upper() == 'YES':
            worksheet = workbook.sheet_by_name(row[0].value)
            tests = worksheet.get_rows()
            toRun = list(set([str(test[0].value) + '.py' for test in tests if not test[0].value == 'TestCase' and test[0].value]))
            final += [*toRun]
    return final
