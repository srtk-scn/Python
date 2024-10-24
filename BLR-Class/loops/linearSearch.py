# WAP to demonstrate the linear search algoritham also print the index

a=[4,5,6,2,4,8,9,2,1]
key=8
# def linear_search(key,coll):
#     if key not in coll:
#         return 'element not present'
#     for i in range(len(coll)):
#         if key==coll[i]:
#             return 'element present at index {}'.format(i)
# print(linear_search(key,a))

def linear_search(key,coll,start=0,end=0):
    if end==0 or end>len(coll):
        end=len(coll)
    if key not in coll[start:end]:
        return 'element not present'
    for i in range(start,end):
        if key==coll[i]:
            return 'element present at index {}'.format(i)
print(linear_search(key,a,2,7))