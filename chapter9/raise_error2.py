def add(a,b):
    if (type(a) is int and type(b) is int):
        return a+b
    raise ValueError('you have enterned other than integer datatype')
print(add('gdg','sas'))                       #we want that function adds only the integers values
# print(add(5,8))