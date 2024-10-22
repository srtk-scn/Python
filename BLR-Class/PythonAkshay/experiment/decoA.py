def outer(func):
    print("control enterned into outer function")
    print("value in func is", func)
    def inner(arg):
        print("control enterned into the the inner function")
        print("value in the arg", arg)
        print("before task")
        func(arg)
        print("after task")
        print("control is leaving inner")
    print('CONTROL IS LEAVING OUTER')
    return inner
@outer
def sample(name):
    print("control enterned into sample")
    print(name)
    print("control is leaving sample")
# print(sample)
sample("sarthak")