# vegetable and fruits ordering and billing system
menu = {"ladyfinger" : 20,
        "pumpkin" : 15,
        "apple" : 12,
        "guavava" : 30,
        "potato" : 20,
        "cherry" : 15,
        "mango" : 50,
        "chilli" : 10} #Here all prices are for 1 kg
cart = []
total = 0
print("-----------Menu-----------")
for key,value in menu.items():
    print(f"{key:10}: {value}")
    # Here 10 means width of 10 characters which align all characters in one line
    print("------------------------")
while True :
    fruit_or_veggies = input("enter fruit_or_veggies : ")
    if fruit_or_veggies == "q":
      break
    elif fruit_or_veggies in menu :
       cart.append(fruit_or_veggies)
       #Here .get means to find value of something
       print("------------YOUR ORDER-------------")
       for fruit_or_veggies in cart :
                print(fruit_or_veggies,end= " ") 
       total += menu.get(fruit_or_veggies)
           
       print(f"Total is :  {total : .2f} Rupees")
                   
    else:
        print("item not in menu")
    