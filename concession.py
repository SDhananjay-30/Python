
menu = {
    "pizza":3.00,
    "popcorn":5.00,
    "nachos":6.45,
    "fries":10.00,
    "chips":1.00,
    "soda":3.50,
    "lemonade":4.25
}

cart = []
total = 0

print("--------Menu----------")
for key,value in menu.items():
    print(f"{key:10}:${value:2}")
print("------------------------")

while True:
    food = input("Select an item(enter q to end):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------Your Order--------")

for food in cart:
    total += menu.get(food)
    print(food,end=",""\n")

print(f"Total is:${total}")

