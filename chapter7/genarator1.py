# iterables and iterator

l=[1,2,3,4,5,6]      #iterable
print(dir(l))
# for i in l:
#     print(i)
i=iter(l)
print(dir(i))
print(next(i))       #now this is iterator
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for num in map(lambda a:a**2,l):    #iterators
    print(num)

#  generators are similer to iterators






