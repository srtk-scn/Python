def fact(n):
    if n in [0, 1]:
        res = 1
    else:
        res = 1
        for i in range(n, 0, -1):
            res *= i
    print("Factorial of {} is {}".format(n, res))
    return res

print(fact(10))