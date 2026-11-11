import random
emojis = {"r" : "🪨" , "s" : "✂️" , "p" : "📃"}
choices = ("r","s","p")
while True :
    user = input("enter user :")
    if user not in choices :
        print("invalid choice")
        continue
    comp = random.choice(choices)
    print(f"you chose {emojis[user]}")
    print(f"comp chose {emojis[comp]}")
    if(user == comp):
        print("tie")
    elif((user == "r" and comp == "p" or
         user == "s" and comp == "p" or
         user == "p" and comp == "r")):
        print("you win")
    else :
        print("you lose")
    should_continue = input("enter(y/n) :")
    if should_continue == "n" :
           break
    

    