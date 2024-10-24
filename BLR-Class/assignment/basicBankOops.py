class Basic_Bank:
    bname='Basic Bank'
    roi=14
    mbl='mumbai'
    ifsc='0X123'
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.bal=c
    def display(self):
        print("NAME  :",self.name)
        print("AGE  :", self.age)
        print("BAL  :", self.bal)
        print("BNAME  :", self.bname)
        print("ROI  :", self.roi)
        print("MBL  :", self.mbl)
        print("IFSC  :", self.ifsc)
    def deposit(self,amt=0):
        if amt==0:
            amt=self.get_amt()
        self.bal=self.add(self.bal,amt)
        print('deposite done sucessfully for ',self.name,' of ',amt)
        print('#'*50)
    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amt()
        if self.bal>=amt:
            self.bal=self.sub(self.bal,amt)
            print('withdraw done succesfully for ',self.name,'of',amt)
            print('#'*50)
        else:
            print('insufficient balance')
            print('#'*50)
    @classmethod
    def descls(cls):
        print('BANME  :',cls.bname)
        print('ROI  :', cls.roi)
        print('MBL  :', cls.mbl)
        print('#'*50)
    @classmethod
    def modiy_roi(cls,new_roi):
        cls.roi=new_roi
        print('modification of ROI has been done sucessfully with ', new_roi)
        print('#'*50)
    @classmethod
    def modify_bname(cls,new_bname):
        cls.banme=new_bname
        print("modification of bank name has been done sucessfully with ", new_bname)
        print('#'*50)
    @staticmethod
    def get_amt():
        a=int(input('enter the amount for transaction process :'))
        return a
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
class SBIM(Basic_Bank):
    bname='SBIM'
    roi=15
    mbl='Delhi'
    ifsc='0X1234'
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.address=d
class SBIH(Basic_Bank):
    bname='SBIH'
    roi=17
    mbl='Hyderabad'
    ifsc='0X1235'
    def __init__(self,a,b,c,e):
        super().__init__(a,b,c)
        self.address=e
class SBI(SBIM,SBIH):
    bname='SBI'
    roi=18
    mbl='Kanpur'
    ifsc='0X12345'
    def __init__(self,a,b,c,f):
        super().__init__(a,b,c)
        self.address=f
A=Basic_Bank('Sarthak',26,50000)
B=SBIM('karan',25,25000,'pukh')
C=SBIH('Sonal',30,250000,'pukhra')
D=SBIM('Golu',19,2500,'pukhrayan')
A.display()
B.display()
C.display()
D.display()
print(B.address)
print(C.address)
print(D.address)
A.modiy_roi(10)
print(A.roi)
D.withdraw(500)
D.display()


