# can we derive more than one class from base class
# multilevel inheritance
# method resolution order(MRO)
# method Overiding
# isinstance(),issubclass()

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model=model_name
        self._price=max(price,0)

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphone(Phone):   #child/deried class
    def __init__(self,brand,model_name,price,ram,int_memory):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.int_memo=int_memory
    def full_name(self):
        return f"{self.brand} {self.model} and price is{self._price} and with{self.int_memo} internal memory @ {self.ram}RAM"
class Basic(Phone):   #child/deried class
    def __init__(self,brand,model_name,price,ram,int_memory):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.int_memo=int_memory
    def full_name(self):
        return f"{self.brand} {self.model} and price is{self._price} and with{self.int_memo} internal memory"

class FlagshipPhone(Smartphone):   #child/deried class
    def __init__(self,brand,model_name,price,ram,int_memory,rear_camera):
        super().__init__(brand,model_name,price,ram,int_memory)
        self.rear=rear_camera
    def full_name(self):
        return f"{self.brand} {self.model} and price is{self._price} and with{self.int_memo} internal memory & {self.rear} camera"
p1=Phone('Nokia','1100',2500)
p2=Basic('samsung','N90',8500,'1GB',"2GB")
p3=Smartphone('Oneplus','1254',25000,6,64)
p4=FlagshipPhone('iphone','I7852',100000,'4GB','128GB','42MP')
print(p1.full_name())
print(p2.full_name())
print(p3.full_name())
print(p4.full_name())
# print(help(Basic))       #searches for the method in 1.FlagshipPhone2.Smartphone3.Phone4.builtins.object
print(isinstance(p1,Phone))
print(isinstance(p2,Phone))
print(isinstance(p1,Basic))

print(isinstance(p2,Basic))
print(isinstance(p3,FlagshipPhone))
print(isinstance(p4,Basic))
print(isinstance(p4,Smartphone))
