#raise error example 2


class Mobile:
    def __init__(self,name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.mobiles=[]

    def add_mobiles(self,new_phone):
        if isinstance(new_phone,Mobile):
            self.mobiles.append(new_phone)
        else:
            raise TypeError('new phone should be object of Mobile class')

oneplus=Mobile('oneplus6')
samsung='samsung galaxy5'
mobostore=MobileStore()

print(mobostore.mobiles)
mobostore.add_mobiles(oneplus)
mobostore.add_mobiles(samsung)
print(mobostore.mobiles)
mobo=mobostore.mobiles
print(mobo[0].name)