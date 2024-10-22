#static method


class Person:
    count_instance=0  #class variable/class attribute
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first=first_name
        self.last=last_name
        self.age=age
    def full_name(self):
        print(f"{self.first} {self.last}")
    def is_above_18(self):
        return self.age>18
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

    @classmethod
    def string_form(cls,string):
        f1,f2,f3=string.split(',')
        return cls(f1,f2,f3)
    @staticmethod
    def hello():
        print('hello static method called')



p1=Person('sarthak','sachan',25)
p2=Person('shashwat','sachan',15)
print(p1.first)
print(p2.age)
print(p2.full_name())
print(Person.full_name(p2))
print(p1.is_above_18())
print(p2.is_above_18())
print(Person.count_instances())
print(p1.count_instances())
p3=Person.string_form('sarthak,sachan,25')
print(p3.full_name())
Person.hello()
p1.hello()