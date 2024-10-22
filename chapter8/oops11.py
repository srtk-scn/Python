# inheritance >> It is used to import the same properties fron base/parent class to derived/parent class


class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model=model_name
        self._price=price

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"

class Smartphone:
    def __init__(self,brand,model_name,price,ram,int_memory):
        self.brand = brand
        self.model = model_name
        self._price = price
        self.ram=ram
        self.int_memo=int_memory
    def full_name(self):
        return f"{self.brand} {self.model} with {self.ram} GB RAM and internal memory {self.int_memo} GB"





p1=Phone('Nokia','1100',2500)
p2=Smartphone('Oneplus','1254',25000,6,64)
print(p1.full_name())
print(p2.full_name())



# by instance


# class Phone:
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.model=model_name
#         self._price=max(price,0)

#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}")

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# class Smartphone(Phone):   #child/deried class
#     def __init__(self,brand,model_name,price,ram,int_memory):
#         #first way>>>> uncommon
#         # Phone.__init__(self,brand,model_name,price)
#         #second way>>> commom
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.int_memo=int_memory
#     def full_name(self):
#         return f"{self.brand} {self.model} with {self.ram} GB RAM and internal memory {self.int_memo} GB"





# p1=Phone('Nokia','1100',2500)
# p2=Smartphone('Oneplus','1254',25000,6,64)
# print(p1.full_name())
# print(p2.full_name()+ f" and price is {p2._price} with internal memory {p2.int_memo}")
