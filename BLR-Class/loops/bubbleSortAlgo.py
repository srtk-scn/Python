#program to demonstrate bubble sort algorithm
#1>.consider a mutual colection
#2>.consider e elements from the begining and comapre
#if ascending order [>] else [<] with its next element
#if the condition is satisfied then swp the number
#repet the step 2 and step 3 till the last sorted elements
#repeat the proces from step 2 to step 4 for n-1
#times       [n is the length of collection]

# a=[5,1,3,6,4,2]
# for passno in range(1,len(a)):
#     for i in range(0,len(a)-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
#         print(a)

# f=[5,1,3,6,4,2]
# def bubble(a):
#     for passno in range(1,len(a)):
#         for i in range(0,len(a)-1):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
#     return a
# print(bubble(f))
# print(bubble(['rat','bat','cat','dog']))


z=[7,8,9,4,5,6,6,23,1,4,5]
def bubble(b):
    for passno in range(1,len(b)):
        for i in range(0,len(b)-1):
            if b[i]>b[i+1]:
                b[i],b[i+1]=b[i+1],b[i]
    return b
print(bubble(z))