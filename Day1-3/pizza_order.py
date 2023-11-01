print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size == "S":
    price += 600
elif size == "M":
    price += 800
else:
    price +=1200


if add_pepperoni == "Y":
    if size=="S":
        price += 150
    else:
        price += 250

if extra_cheese == "Y":
    price += 75

print(f"Your final bill is Rs.{price}")
