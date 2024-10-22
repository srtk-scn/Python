user={'name':'sarthak','age':18}
print(user)
print(type(user))


user=dict(name='sarthak',age=18)
print(user)
print(type(user))
#
if 'name' in user:
    print('present')
else:
    print('not present')
# #
if 18 in user.values():
    print('present')
else:
    print('not present')
for i in user:
    print(i)
for i in user.values():
    print(i)
for i in user.keys():
    print(i)
for key,values in user.items():
    print(key,values)
more=dict(sex='male')
user.update(more)
print(user)

# fromkeys

a=dict.fromkeys(range(1,11),['unknown','unknown'])
print(a)
print(user.get('name'))
user2=user.copy()
print(user2)
print(user==user2)
user=user2
if user is user2:
    print("same address")
else:
    print('diff add')
user2.clear()
print(user)
print(user.get('names','not found'))

def word_count(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
print(word_count('sarthak'))

k={}
name=input("enter name:")
age=input("enter age:")
sex=input("enter sex")
songs=input("enter your movies").split(",")
k['name']=name
k['age']=age
k['sex']=sex
k['sung']=songs
print(k)
for i,j in k.items():
    print(f" keys {i} and value {j} ")

k={}
def count_char(s):
    for i in s:
        k[i]=s.count(i)
    return k
print(count_char('sarthak'))
for i,j in k.items():
    print(f"key={i} and values {j}")