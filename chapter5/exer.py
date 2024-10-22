#try to make a function in one giing the average of the corresponding elements in sublist respectively






# def average_finder(l1,l2):
#     average=[]
#     for pair in zip(l1,l2):
#         print(pair)
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3,5,4],[7,8,4,5,7]))


# def average_finder(*l):
#     average=[]
#     for pair in zip(*l):
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3,5,4],[7,8,4,5,5],[5,7,5,1]))

# avg=lambda *l:[sum(pair)/len(pair) for pair in zip(*l)]
# print(avg([1,2,3,5,4],[7,8,4,5,5],[5,7,5,1]))



avg=lambda *a:[sum(pair)/len(pair) for pair in zip(*a)]
print(avg([1,2,3,5,4],[7,8,4,5,5],[5,7,5,1]))
# def sample(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     print('*'*80)
# a={'a':1,'b':2,'c':3}
# sample(**a)
# sample(*a)