# def sample(*a):
#     print(a)
#     print(type(a))
#     print(*a)
#     print("_"*30)
# sample(1,2,3,56,4)
# sample(1,2)
# sample()
# sample(1,2,3,56,4,54,56,7,5)


def sample(**a):
    print(a)
    print(*a)
    print(type(a))
    print("_"*30)
sample(a=1,b=2,c=3,d=4)
sample(ename="raju",eid=4587,ephone=456345265)
sample(ename="raju",eid=4587,ephone=456345265,email="sarthak@gsdfjaghv.com")
