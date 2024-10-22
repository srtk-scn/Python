# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
sqr= [i**2 for i in range(1,10) if i%2==0]
print(sqr)
#by list comprehension aproach

# squares2= [i**2 for i in range(1,11) if i%2==0]
# print(squares2)

square=[i**2 for i in range(1,11)]
print(square)

negative=[-i for i in range(1,11)]
print(negative)

l=['sartyhak','karan','golu']
p=[i[0] for i in l]
print(p)

# z=['abc','pqr','xyz']
# w=[i[::-1] f
print([i[::-1] for i in ['abc','pqr','xyz']])
print([i for i in range(1,11) if i%2==0])

q=[1, 4, 9, 16, 25, 36,55.0,68.15,'dasgsd',[1,2,5,8,'sar'],True,False]
# print([str(i) for i in q if type(i)==int or type(i)==float])
# print([i*2 if (i%2==0) else -i for i in range(1,11)])
print([str(i) for i in q if type(i)==int or type(i)==float])

nested=[[i for i in range(1,4)] for j in range(3)]
print(nested)

nest=[[i for i in range(3)] for j in range(4)]
print(nest)