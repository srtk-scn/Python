# fruits=['grapes','mango','apple']
# print(fruits.sort(reverse=True))
# print(dir(fruits))
# print(fruits)
# print(sorted(fruits))


# # fruits1=('grapes','mango','apple')
# # # fruits1.sort()
# # print(sorted(fruits1))



# fruits2={'grapes','mango','apple'}
# # print(sorted(fruits2,reverse=True))
# list(fruits2).sort()
# print(fruits2)


student2=[
        {'score':90,'age':25},
        {'score':60,'age':24},
        {'score':500,'age':20}
    ]
print(sorted(student2,key=lambda d: d['score'],reverse=True))