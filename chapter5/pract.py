# user_id=['user1','user2','user3']
# names=['sarthak','golu','karan']
# last_names=['sachan','cslflhl','yegfhg']

# print(list(zip(user_id,names,last_names)))
# print(dict(zip(names,last_names)))
l=[(1,2),(3,4),(5,6),(7,8)]
# l1,l2=list(zip(*l))
# print(l1)
# print(l2)
l1,l2=list(zip(*l))
print(l1,l2)
new=[]
for i in zip(l1,l2):
    new.append(max(i))
print(new)
