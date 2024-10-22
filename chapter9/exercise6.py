def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print('you cananot divide a numbeer by zero')
        print(err)
    except TypeError as err:
        print("number must be in integer and float type")
    except:
        print("unexpected error")
print(divide(10,0))