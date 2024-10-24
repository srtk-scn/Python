class School:
    sname='M.P.S.'
    nob=2
    mbl='PUKHRAYAN'
    def __init__(self,a,b,c,d):
        self.name=a
        self.age=b
        self.job=c
        self.fees=d
    def display(self):
        print("NAME  :",self.name)
        print("AGE  :", self.age)
        print("JOB  :", self.job)
        print("Fees  :", self.fees)
        print("SNAME  :", self.sname)
        print("NOB  :", self.nob)
        print("MBL  :", self.mbl)
    def fee_deposit(self,amt=0):
        if amt==0:
            amt=self.get_amt()
        self.fees=self.add(self.fees,amt)
        print('fee deposite done sucessfully for ',self.name,' of ',amt)
        print('#'*50)
    def salary_given(self,amt=0):
        if amt==0:
            amt=self.get_amt()
            self.fees=self.sub(self.fees,amt)
            print('salary given succesfully for ',self.name,'of',amt)
            print('#'*50)
    @classmethod
    def descls(cls):
        print('SANME  :',cls.bname)
        print('NO of Branches  :', cls.roi)
        print('MBL  :', cls.mbl)
        print('#'*50)
    @classmethod
    def modiy_nbl(cls,new_nbl):
        cls.roi=new_nbl
        print('modification of No of Branches has been done sucessfully with ', new_nbl)
        print('#'*50)
    @classmethod
    def modify_sname(cls,new_sname):
        cls.sname=new_sname
        print("modification of School name has been done sucessfully with ", new_sname)
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
dinga=School('dinga',20,'student',2000)
dingi=School('dingi',60,'teacher',25000)
dinga.display()
dingi.display()
dinga.fee_deposit()
print(dinga.fees)
dingi.salary_given(0)
