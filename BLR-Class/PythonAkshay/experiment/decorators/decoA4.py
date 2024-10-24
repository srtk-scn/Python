def load(main_task):
    def inner(args):
        print("load the vehicle=", args)
        main_task()
        print("unload the vehicle=", args)
    return(inner)
@load
def vehicle():
    print("travel")
vehicle("truck")
vehicle("car")
vehicle("bus")