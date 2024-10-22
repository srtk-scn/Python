#exercise>>  make a class having laptops as object and also define a method to apply discount as instance variable


class Laptop:
    def __init__(self,laptop_name,brand_name,model_name,price):
        self.name=laptop_name
        self.bname=brand_name
        self.mod_num=model_name
        self.pric=price
        self.full=laptop_name+" "+brand_name
    def apply_dis(self,num):
        dis=num*self.pric/100
        return self.pric-dis

l1=Laptop('achgfdk','acer',42424,254225)
l2=Laptop('sdjkhfk','sacghan',545275,50000)
print(l1.full)
print(l1.apply_dis(20))
print(l2.apply_dis(20))
print(Laptop.apply_dis(l2,10))
print(Laptop.apply_dis(l1,20))