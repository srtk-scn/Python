# has a relationship
class A:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        print("constructor of A")
    def __str__(self):
        return "{}{}".format(self.x,self.y)
    def __add__(self,other):
        x=self.x + other
        y=self.y + other
        return A(x,y)
    # def __sub__(self,other):
        
    def disp(self):
        print("disp of parent")
        print(self)
oa=A(10,20)
print(str(oa))
print(oa.__add__(8))


# class B:
#     c=15
#     d=25
#     # oa=A(2)
#     def __init__(self,y):
#         self.y=y
#         print("Constuctor of B")
#     def disp(self):
#         print("disp method of child")
# class C(A,B):
#     a,b=14,19
#     def __init__(self,x,y,z):
#         self.z=z
#         A.__init__(self,x)
#         B.__init__(self,y)
#         print("C of C")
# # oa=A(25)
# # ob=B(26)
# oc=C(58,55,88)
# print(oc.disp(),oc.a,oc.b,oc.c,oc.d)
