class Person:
    count_instance=0
    def __init__(self,first,last,age):
        Person.count_instance+=1
        self.f=first
        self.l=last
        self.a=age
        self.full=first + last

    def reverse_name(self):
        return self.f[::-1]
    def is_above_18(self):
        return self.a>18
    @classmethod
    def string_form(cls,string):
        f1,f2,f3=string.split(",")
        return cls(f1,f2,f3)
p1=Person('sarthak','sachan',26)
p2=Person('shashwat','sachan',15)
# print(Person.reverse_name(p1))
# print(p1.reverse_name())
# print(Person.count_instance)
# print(p2.is_above_18())
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
# p3=Person.string_form("anupam,jadon,28")
# print(p3.reverse_name())
# print(Person.count_instance)