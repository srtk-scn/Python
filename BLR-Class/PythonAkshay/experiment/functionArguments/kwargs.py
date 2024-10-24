def sample(*args,**kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    print("_"*30)
sample(1,2,3,4,5,6,7,8,9)
sample(1,2,3,4,5,a=6,b=7,c=8,d=9)
sample(1,2,3,4,5,'hai',[1,2,3],(1,2,3),a=6,b=7,c=8,d=9)
sample(a=6,b=7,c=8,d=9)
sample()

    