foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy\n")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")
print("")
for price in prices:
    print(price, end=" ")
print("")
print("-----YOUR TOTAL-----")
total = 0
for price in prices:
    total += price

print(total)


