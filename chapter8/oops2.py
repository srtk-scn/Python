#instance methods >>  those functions which are defined under a class are called methods
l=[1,2,3,4,5,6]
l.append(10)  #append is a method which is defined under list class.
list.append(l,10)

print(l)
#clear,pop
l.clear()
print(l)
list.clear(l)
print(l)


class Person:
    a=1
    b=2
    def __init__(self,first_name,last_name,age):
        self.first=first_name
        self.last=last_name
        self.age=age
    def full_name(self):
        print(f"{self.first} {self.last}")
    def is_above_18(self):
        return self.age>18



p1=Person('sarthak','sachan',25)
p2=Person('shashwat','sachan',15)
print(p1.first)
print(p2.age)
print(p2.full_name())
print(Person.full_name(p2))
print(p1.is_above_18())
print(p2.is_above_18())
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
p2.b=20
Person.b=30
print(p2.b)
print(p1.b)
