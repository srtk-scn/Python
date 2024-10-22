# name=['abc','agdfadjhbc','sarthak']
# pos=0
# for i in name:
#     print(f"position of {pos} is ------>{i}")
#     pos+=1
# # by enumarate function

# for i,n in enumerate(name):
#     print(f"position of {n} is ------>{i}")
#
name=['abc','agdfadjhbc','sarthak']
# def trace(l,target):
#     for i,j in enumerate(target):
#         if j==l:
#             return i
#     return -1
# print(trace('sarthak',name))

track(name,"sarthak")
def trace(x,tar):
    for j,k in enumerate(x):
        if k==tar:
            return j
    return -1 
# print(trace(name,'sarthak'))       
