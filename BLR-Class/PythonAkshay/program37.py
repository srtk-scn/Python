# write a program to take number and find the factorial of it and print it.

def fact(n):
    if n in [0,1]:
        res=1
        print(res)
    else:
        res=1
        for i in range(n,0,-1):
            res =res*i
    print("factorial of {} is {}".format(n,res))
fact(5)
    
