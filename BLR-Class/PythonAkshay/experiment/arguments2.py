# def add(a,b,c=0,d=0,e=0):
#     return print(a+b+c+d+e)
# # result= add(10,20)
# # print(result)
# add(10,20)
# add(10,20,30)
# add(10,20,30,40)
# add(10,20,30,40,50)
# add("Hello","World")

def add(a,b,c=0,d=0,e=0):
    if c==0 and d==0 and d==0:
        return a+b
    if d==0 and e==0:
        return a+b+c
    if e==0:
        return a+b+c+d
    return a+b+c+d+e
print(add("hello","world"))