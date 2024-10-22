def is_armstrong(n):
    sum=0
    for i in str(n):
        sum+=int(i)**3
    return sum==n
