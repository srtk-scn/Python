# 1encapsulation>>make easy to read "gather the useful data(methods) at a single place
# 2abtraction>>hide the complexity of a function i.e..how the logic works  {ex>> in list class how the sort function logic works}
# 3some special naming convention>>in other programming languages some methods are public and private but in python all are public,
# so some convetions are given to understand all the developers that it is private method dont make changes to it.

# 4Name mangling>> not a convention __name

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model=model_name
        self.__price=price                           #convention of private name

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand}{self.model}"
    def send_message(self):
        pass #twilio
phone1=Phone('nokia',1100,15000)
print(phone1._Phone__price)                      #name mangling
print(phone1.__dict__)
print(Phone.make_a_call(phone1,7011785707))
