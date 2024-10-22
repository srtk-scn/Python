
#multiple inheritance>>it is a order of executing the same function in different classes..

class A:
    def instance_method_a(self):
        return 'welcome to instance method a'
    def hello(self):
        print('Hello method from class A')

class B:
    def instance_method_b(self):
        print('welcome to instance method b')
    def hello(self):
        print('Hello method from class B')

class C(B,A):
    pass


instance_c=C()
print(instance_c.instance_method_a())
print(instance_c.hello())
print(help(C))
print(C.mro())
print(C.__mro__)