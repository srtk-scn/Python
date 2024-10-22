numbers=[1,2,3,45,67,8,9]
print(min(numbers))
print(max(numbers))

names=['sarthak','karan','gdfbfnfgmnolu','rishabhvjhkjbvkjd']
print(max(names))    #according to length
def func(items):
    return len(items)
print(max(names,key=func))
print(max(names,key=lambda item:len(item)))

students=[
    {'name':'sarthak','score':90,'age':25},
    {'name':'karan','score':60,'age':24},
    {'name':'golu','score':500,'age':20}
]
print(max(students,key=lambda items: items.get('score'))['name'])
print(max(students,key=lambda items: items.get('age'))['name'])
student2={
    'sarthak':{'score':90,'age':25},
    'karan':{'score':60,'age':24},
    'golu':{'score':500,'age':20}
    }
print(max(student2,key=lambda item:student2[item]['score'] ))