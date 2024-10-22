# function with no arguments and no return value
def fact():
    n=5
    result= 1
    for i in range(n,0,-1):
        result= result*i
    print("factorial of {} is {}".format(n,result))
fact()