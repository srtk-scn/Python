#WAP to reverse a number
def reverse(a):
    rev=0
    while a!=0:
        ld=a%10
        a=a//10
        rev=rev*10+ld
    return rev
k=int(input('enter the number'))
print(reverse(k))
