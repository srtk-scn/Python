#object oriented programming
#we can create our own object
#oject is created under the class having the same blueprint as defined in that particular class

l1={1,2,3,4,5}       #list object under a class having the blueprints of list
l2=[7,8,9,4,5,6]         #list object under a class having the blueprints of list
l3=['sarthak','sachan']      #list objects having different strings having some class


#defining a class
class Person:
    def __init__(self,first_name,last_name,age):
        print('CALLING INIT OR CONSTRUCTOR FUNCTION TO MAKE AN OBJECT')
        self.firstname=first_name
        self.lastname=last_name
        self.age=age

p1=Person('sarthak','sachan',25)
# p2=Person('shashwat','sachan',20)

print(p1.firstname)
# print(p2.age)

class Laptop:
    def __init__(self,brand_name,model_num,price):
        print('calling a constructor function')
        self.brand=brand_name
        self.mod=model_num
        self.pric=price
        self.modelnew=brand_name + " " + str(model_num)
l1=Laptop('HP',54634,436534)
l2=Laptop('acer',57443,38574)

print(l1.brand)
print(l1.modelnew)
print(l2.mod)
print(l2.pric)

class Person:
    a=10
    b=20
    def __init__(self,name,caste,religion,citizen):
        self.name=name
        self.caste=caste
        self.religion=religion
        self.citizen=citizen

p1=Person('sarthak','kurmi','hindu','indian')
p2=Person('karan','kurmi','hindu','krgystan')

print(p1.name)
print(p2.name)
print(p1.a)
p1.a=100
print(p1.a)
