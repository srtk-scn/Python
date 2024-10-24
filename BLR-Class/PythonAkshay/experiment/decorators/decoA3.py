def wash(main_task):
    def inner():
        print("wash your hands")
        main_task()
        print("wash your hands after")
    return inner

@wash
def break_fast():
    print("have a breakfast")
@wash
def lunch():
    print("have a lunch")
@wash 
def dinner():
    print("have dinner")
break_fast()
lunch()
dinner()