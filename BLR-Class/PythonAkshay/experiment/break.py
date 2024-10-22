# modified number guessing game
# a= int(input("guess a number between 0 and 100:"))
# w=56
# while True:
#     if a==w:
#         print("you WIN!")
#         break
#     elif a>w:
#         print("too high")
#         a=int(input("guess again:"))
#     else:
#         print("too low")
#         a=int(input("guess again:"))
                            # or
# a= int(input("guess a number between 0 and 100:"))
# w=56
# t=0
# while True:
#     if a==w:
#         t+=1
#         print("you WIN! in times",t)
#         break
#     elif a>w:
#         print("too high")
#         t+=1
#         a=int(input("guess again"))
#         continue
#     else:
#         print("too low")
#         t+=1
#         a=int(input("guess again"))
                            # or
# win=56
# guess= int(input("enter a number between 1 and 100"))
# time=1
# over= False
# while not over:
#     if guess==win:
#         print("you win! in times", time)
#         over= True
#     else:                                                         game logic correct 
#         if guess>win:
#             print("too high")
#             time+=1
#             guess= int(input("guess again"))
#         else:
#             print("too low")
#             time+=1
#             guess= int(input("guess again"))
                                    #OR by dry principle
# win=56
# guess= int(input("enter a number between 1 and 100"))
# time=1
# over= False
# while not over:
#     if guess==win:
#         print("you win! in times", time)
#         over= True
#     else:
#         if guess>win:
#             print("too high")
           
#         else:
#             print("too low")
#     time+=1
#     guess= int(input("guess again"))       

# win=56
# guess= int(input("enter a number between 1 and 100"))
# time=1
# while True:
#     if guess==win:
#         print("you win! in times", time)
#         break
#     else:
#         if guess>win:
#             print("too high")
           
#         else:
#             print("too low")
#     time+=1
#     guess= int(input("guess again"))  

import random
win= random.randint(1,100)
time=1
while True:
    guess= int(input("enter a number between 1 and 100"))
    if guess==win:
        print("you win! in times", time)
        break
    else:
        if guess>win:
            print("too high")
           
        else:
            print("too low")
    time+=1
    continue 