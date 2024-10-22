def sample(a,b,c):
    print(a)
    print(b)
    print(c)
    print('-'*30)
a=[1,2,3]
sample(*a)
a='hai'
sample(*a)
a={'a':1,'b':2,'c':3}
sample(**a)
sample(*a)