# shopping cart system
foods = []
prices = []
quantities = []
i = 0
while True :
    food = input("enter a food to buy : ")
    if(food.lower() == "q"):
        break
    else :
        price = float(input("enter price of one item here : "))
        quantity = int(input("enter quantity : "))
        foods.append(food)
        prices.append(price)
        quantities.append(quantity)
        print("--------YOUR CART-------")
        for food in foods:
           print(food,end = " ")
           total2 = 0
           for i in range(len(prices)):
            total1 = prices[i] * quantities[i]
            total2 += total1
        print(total2)