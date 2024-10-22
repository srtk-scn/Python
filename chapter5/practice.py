def outerFunc(func):
    def innerFunc():
        print('this is a awesome funcion')
        func()
    return innerFunc
@outerFunc
def sarthak():
    print('this is sarthak func')
sarthak()
outerFunc(sarthak)