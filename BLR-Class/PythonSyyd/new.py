class head:
    a=10
    def __init__(self,p):
        self.p=p
    def __add__(self,other):
        print('add method got invoked')
        res= self.p + other.p
        return head(res)
    def __sub__(self,other):
        print('subtract method got invoked')
        res= self.p-other.p
        return head(res)
oa=head(20)
print(oa.p)
ob=head(30)
oc=head(50)
a=oa+oc-ob
print(a.p)
