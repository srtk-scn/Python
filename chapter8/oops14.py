#special magic/dunder method>>__str__(),__repr__()
#operator overloading>>+,*
#polymorphism>>more than one form if we + interger it works and also with string it works.+is used for add intergers where in strings it concatinate.


class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.mod=model
        self.price=price

    def phone_name(self):
        return f"{self.brand} {self.mod}"

    # repr,str
    def __str__(self):
        return f"{self.brand} {self.mod} "
    def __repr__(self):
        return f"Phone(\'{self.brand}\',\'{self.mod}\',{self.price})"               #developers make that because when theyreturn they will get the object
    def __len__(self):
        return len(self.phone_name())
    def __add__(self, other):
        return self.price+other.price
l=[1,2,3,4,5]
print(l)
print(len(l))
t=(1,2,3,4,5,6,7,8,9)
print(len(t))
s={1,2,3,4,5,6}
print(len(s))
my_phone=Phone('Nokia','1100',2500)
my_phone2=Phone('Nokia','1600',2600)
# print(my_phone)       #this gives you addess  to make it as list object we should use dunder method
print(my_phone.__str__())
print(my_phone.__repr__())
print(my_phone.phone_name())
print(len(my_phone))                                       #called as function
print(my_phone.__len__())                                  #called as a method
print(my_phone+ my_phone2)