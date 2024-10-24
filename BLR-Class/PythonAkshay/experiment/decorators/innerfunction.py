def outer():
    print("control is in outer function")
    # print(inner)
    def inner():
        print("control is in inner function")
        print("control leaving inner function")
    inner()
    print("control leaving outer function")
outer()
