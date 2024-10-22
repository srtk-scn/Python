#break statement

i=0
while True:
    if i==10:
        print("break is getting executed")
        break
    print(i)
    i+=1

for i in range(10):
    if i==5:
        print("time to break")
        break
    print(i)
    i+=1