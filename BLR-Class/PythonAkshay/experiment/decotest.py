def browser_support(func):
    def inner():
        print("open the browser")
        print("go to url")
        func()
        print("close the browser")
        print("_"*50)
    return inner
@browser_support
def cucp():
    print("correct username and correct password")
    print("click on login")
@browser_support
def cuwp():
    print("correct username and pasword")
    print("click on log in")
@browser_support
def wucp():
    print("wrong username and correct pasword")
    print("click on log in")
@browser_support
def wuwp():
    print("wrong username and pasword")
    print("click on log in")
cucp()
cuwp()
wucp()
wuwp()
