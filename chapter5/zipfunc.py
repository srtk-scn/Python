#  zip function

user_id=['user1','user2','user3']
names=['sarthak','golu','karan']
last_names=['sachan','cslflhl','yegfhg']

print(list(zip(user_id,names,last_names)))
print(dict(zip(user_id,last_names)))
# print((dict(zip(user_id,names,last_names))))
for i,j,k in zip(user_id,names,last_names):
    print(f"name of {i} is {j} {k}")
print(list(zip(user_id,names,last_names)))
# unzip function

# l1=[1,3,65,7]
# l2=[2,4,6,8]

l=[(1,2),(3,4),(5,6),(7,8)]
print(*l)
print(list(zip(*l)))
# l=[]
# for i in zip(l1,l2):
#     print(max(i))
l1,l2=list(zip(*l))
print(l1)
print(l2)
# newlist=[] 
# for i in zip(l1,l2):
#     newlist.append(max(i))
# print(newlist)
# for i in zip(l1,l2):
#     newlist.append(max(i))
# print(newlist)

# def function1(s,f):
#     a=""
#     if f==0:
#         for i in s[1:len(s):2]:
#             a+=i
    
#     else:
#         for i in s[0:len(s):2]:
#             a+=i             
#     return a

def function1(s,f):
    if f:
        return s[0:len(s):2]
    return s[1:len(s):2]

print(function1('TRACXN',0))    
print(function1('TRACXN',1))  