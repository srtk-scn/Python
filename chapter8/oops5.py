class Person:
    count = 0
    def __init__(self,first_name,Last_name):
        Person.count+=1
        self.first=first_name
        self.last=Last_name
    def full_name(self):
        print(f"{self.first} {self.last}")
p1=Person('sarthak','sachan')
p2=Person('sarthak','sachan')
p3=Person('sarthak','sachan')
p4=Person('sarthak','sachan')
p5=Person('sarthak','sachan')
print(Person.count)
print(Person.full_name(p1))
