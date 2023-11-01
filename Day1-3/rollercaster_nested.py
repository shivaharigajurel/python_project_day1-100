print("Welcome to the rollercoaster")

height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You Can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12212:
        print("You should pay Rs.500 to ride the rollercaster")
    elif age <= 18:
        print("You should pay Rs.700 to ride the rollercaster!")
    else:
        print("You should pay Rs.1500 to ride rollercaster!")
else:
    print("You Can`t ride the rollercoaster!")