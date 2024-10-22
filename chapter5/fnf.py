# def great(a,b):
#     if a>b:
#         return a
#     return b
# def greatest(a,b,c):
#     # bigger=great(a,b)
#     return great(great(a,b),c)
# print(greatest(1,88,665))

# def is_palindrome(word):
#     return word==word[::-1]
# print(is_palindrome("naman"))
# print(is_palindrome(("saras")))

# def fabbonaci(n):
#     a=0
#     b=1
#     if n==1:
#         print("a")
#     elif n==2:
#         print(a,b,end=" ")
#     else:
#         print(a,b,end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=" ")
# print(fabbonaci(20))
# def square_list(l):

# def neg_list(l):
#     neg=[]
#     for i in l:
#         neg.append(-i)
#     return neg
# print(neg_list(list(range(1,11))))

# def reverse(l):
#     rev=[]
#     for i in l[::-1]:
#         rev.append(i)
#     return rev
# print(reverse(list(range(1,11))))

# def rever(l):
#     r_list=[]
#     for i in range(len(l)):
#         # print(len(l))
#         # print(i)
#         popped_item=l.pop()
#         r_list.append(popped_item)
#         # print(r_list)
#     return(r_list)
# print(rever(list(range(1,11))))


# def revrev(r):
#     j=[]
#     for i in r:
#         j.append(i[::-1])
#     return j
# print(revrev(['abc','tuv','xyz']))

# def oddevensep(l):
#     q=[]
#     w=[]
#     for i in l:
#         if i%2==1:
#             q.append(i)
#         else:
#             w.append(i)
#     return [q,w]
# print(oddevensep(list(range(1,10))))

def commom_finder(b,c):
    a=[]
    for i in b:
        for j in c:
            if i==j:
                a.append(i)
    return a
print(commom_finder([1,2,3,4,5,6,7],[5,6,7,2,4,9,8,10]))
# def commom_finder(b,c):
#     a=[]
#     for i in b:
#         if i in c:
#             a.append(i)
#     return a
# print(commom_finder([1,2,3,4,5,6,7],[5,6,7,2,4,9,8,10]))

def maxdiff(l):
    return max(l)-min(l)
print(maxdiff([4,5,8,69,14]))

def nolist(l):
    c=0
    for i in l:
        if type(i)==list:
            c+=1
    return c
a=[1,2,[3,4,5],[8,6,5,4],'fadh',{1,2,3}]
print(nolist(a))

sarthak= 'sachan','karan','golu'
print(type(sarthak))

c=('sachan','karan','golu')
c1,c2,c3=c
print(c1)
print(c2)
print(c3)
c=(1,2,3,6,5,4,7,8)
print(sum(c))

def func1(a,b):
    add =a+b
    mul=a*b
    return add,mul
c,d=func1(5,4)
print(c)
print(d)
