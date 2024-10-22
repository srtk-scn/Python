# filter function
# def is_even(i):
#     return i%2==0
numbers=[2,56,87,6,1,6,2,4,4]
# evens= list(filter(lambda a: a%2==0,numbers))
# print(evens)
# # for i in evens:
# #     print(i)
# # for i in evens:
# #     print(i)
even= list(lambda a: a**2,numbers)
print(even)


# ev=(filter(lambda a: a%2==0,numbers))
# for i in ev:
#     print(i)

numbers=[2,56,87,6,1,6,2,4,4]
iterator_object=(iter(numbers))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))

map_object=(map(lambda a: a**2,numbers))
print(map_object)
print(next(map_object))
print(next(map_object))
print(next(map_object))

filter_object=(filter(lambda a: a%2==0,numbers))
print(filter_object)
print(next(filter_object))
print(next(filter_object))
print(next(filter_object))
print(next(filter_object))