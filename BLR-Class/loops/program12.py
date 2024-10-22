#write a program to find the nth factorial
def factorial(n):
    res=1
    for i in range(n,0,-1):
        res=res*i
    return res
print(factorial(5))
#wrie a program to print the series of the factorial number between the m to n