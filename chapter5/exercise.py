# def to_power(num,*args):
#     print(*args)
#     print(args)
#     if args:
#         return [i**num for i in args]
#     else:
#         return "you didn't pass args"
# a=[5,8,6,3,1,4,7]
# print(to_power(5,*a))


#
#
# # kwargs

# def func(**kwargs):
#     print(*kwargs)
#     print(**kwargs)
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(f"first{k}:{v}")

# # f=dict(name='sarthak',last="sachan")
# d={'name': 'sarthak', 'last': 'sachan'}
# func(**d)

# print(f)


# def fcap(args):
#     return [i.title() for i in args]
# k=['sarthak','JGJHVjhv']
# print(fcap(k))


# def rfcap(l,**kwargs):
#     if kwargs.get('reverse_str')==True:
#         return [i[::-1].title() for i in l]
#     else:
#         return [i.title() for i in l]
# w=['sarthak','sachan','golu','sachan']
# print(rfcap(w,reverse_str=False))