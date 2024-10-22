class bank:
    bname='SBI'
    roi=14
    mbl='mumbai'
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
dinga=bank('dinga',25,25000)
dingi=bank('dingi',24,40000)
# dinga.display()
# dingi.display()
# dinga.deposit(0)
# print(dinga.bal)
# dingi.deposit(500)
# print(dingi.bal)
# dinga.withdraw(4000525)
print(dinga.bal)
bank.deposit(dingi,500)
print(bank.add(500,1000))

