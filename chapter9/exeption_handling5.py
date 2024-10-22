# #exeeptiion handling
# #try execpt else finally
# while True:
#     try:
#         age=int(input('enter your age'))
#         break
#     except ValueError:
#         print("may be you have entered string of a number,Try again")
#     except:
#         print("unexpected error")


# if age>18:
#     print('you cam play this game')
# else:
#     print('you can\'t play this game')




#else and finally clause in exception handling

while True:
    try:
        number=int(input("enter the number "))
    except ValueError:
        print('may be you have entered other than integer')
    except:
        print('unexpected error')
    else:
        print(f"you have enterned{number}")             #when there is no exeception
        break
    finally:
        print('finally blocks.....')          #always execute