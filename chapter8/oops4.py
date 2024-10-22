# class variable>>  it is same for all the object in a class
class Circle:
    def __init__(self,radius,pi):
        self.rad=radius
        self.pi=pi

    def circum(self):
        return self.pi*self.rad*2                     #pi as a instance variable
c1=Circle(4,3.14)
c2=Circle(5,3.14)
print(c1.circum())
print(c2.circum())          #there is no need to give value everytimr we want ro calculate cicumference




# class variable>>  it is same for all the object in a class
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.rad=radius


    def circum(self):
        return Circle.pi*self.rad*2                    #class variable
c1=Circle(4)
c2=Circle(5)
print(c1.circum())
print(c2.circum())          #there is no need to give value everytimr we want ro calculate cicumference

# exercise>>>  laptop as a class and apply 10% discount as class variable on all products

#exercise>>  make a class having laptops as object and also define a method to apply discount


class Laptop:
    dis=10
    def __init__(self,laptop_name,brand_name,model_name,price):
        self.name=laptop_name
        self.bname=brand_name
        self.mod_num=model_name
        self.pric=price
        self.full=laptop_name+" "+brand_name
    def apply_dis(self):
        disc=Laptop.dis*self.pric/100
        return self.pric-disc
# Laptop.dis=50                                     #for changing the dis percentage for all
l1=Laptop('achgfdk','acer',42424,254225)
l2=Laptop('sdjkhfk','sacghan',545275,50000)
print(l1.full)
print(l1.apply_dis())
l2.dis=50                                        #for changing discount for laptop2>>>also change to classname in function to self
print(l2.apply_dis())
print(Laptop.apply_dis(l2))
print(l1.__dict__)