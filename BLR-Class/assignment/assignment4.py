# Multilevel inheritance in python

class Car:
    now=4
    def __init__(self,a,b,c):
        self.brand=a
        self.model=b
        self.price=c
    def full_name(self):
        print(f"{self.brand} {self.model}")
    def