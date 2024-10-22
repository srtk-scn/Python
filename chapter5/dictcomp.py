# square={i:i**2 for i in range(1,11)}
# print(square)
# print(type(square))
# square2={f"square of {i} is" :i**2 for i in range(1,11)}
# print(square2)
# for k,v in square2.items():
#     print(f"{k} : {v}")

# s="sarthak"
# word_count={f"no of {i} is" : s.count(i) for i in s}
# print(word_count)

# odd_even={i:('even' if i%2==0 else 'odd') for i in range (1,11)}
# print(odd_even)

# even_no = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(even_no)
# print({f'square of {i} : {i**2}' for i in range(1,11)})


a={"a":1,"b":2,"c":3}
b={}
for i,j in reversed(a.items()):
    b[i]=j   
print(b)  

print({for i,j in reversed(a.items())})