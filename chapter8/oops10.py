
# property setter decorator>>it is used to make change in the input if the user enters wrong input if -ve price is enter then converted in to +ve
#if we want to update the price then we have to use @property decorator then @price setter to change the price into +ve when we updated the price







class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model=model_name
        self._price = max(price, 0)
        # if price>0:
        #     self._price=price
        # else:
        #     self._price=0

        # self.complete_spec=f"{self.brand} {self.model} rs{self._price}"

    @property
    def complete_spec(self):
        print(f"{self.brand} {self.model} rs{self._price}")

    # @property
    # def price(self):
    #     return self._price

    # @price.setter
    # def price(self, new_price):
    #     self._price = max(new_price, 0)

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand}{self.model}"

phone1=Phone('nokia','1100',15000)
print(phone1._price)                      #name mangling
print(phone1.__dict__)
phone1.price=-200
print(phone1.price)
print(phone1.complete_spec)

