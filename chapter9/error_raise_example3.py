#raise error example
#non implemented Error
# abstract method in java but same as non implemented error in python


class Animal:
    def __init__(self,name):
        self.naam=name

    def sound(self):
        raise NotImplementedError("you have define this method in subclas")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.brd=breed
    def sound(self):
        return 'bhow bhow'
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.bred=breed

    def sound(self):
        return 'meow meow'

c1=Cat('cherry','indian')
d1=Dog("jack","german")
print(d1.sound())
print(c1.sound())
