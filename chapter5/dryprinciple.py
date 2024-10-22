
guess=1
win=45
while True:
    number = int(input("enter a number between 1 to 100"))
    if number==win:
        print(f"you win the game in {guess} times")
        break
    else:
        if number<=win:
            print("too low")
        else:
            print("too high")
        guess+=1
        continue
