#Fruit crushing game
import random
characters = ["🍎","🍒","🥭","🍌","🍉","🍓","🧆","🍇"]
while True :
 user = input("enter your choice : ")
 comp = random.choices(characters)
 print(f"user chose {user}")
 print(f"computer chose {comp}")
 if user not in characters :
   print("choose only from characters")
   break
 if user == comp:
      print("Crush,it matches")
 if user != comp :
     print("try again")
 
 