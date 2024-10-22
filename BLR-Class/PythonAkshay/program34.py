# return value
# get function

# def get_ab():
#     a,b=10,20
#     return a,b
    
# a,b= get_ab()
# print(a,b)



def fact():
    n=4
    if n in [0,1]:
        print("bye bye")
        return 1
    result=1
    
    for i in range(n,0,-1):
        result*= i
    return result
result= fact()
print(result)
       