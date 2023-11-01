print("Welcome to the rollercoaster")

height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You Can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age<12:
        bill=500
        print(f"child tickets price are Rs.{bill}")
    elif age <= 18:
        bill=700
        print(f"Youth tickets price are Rs.{bill}")
    else:
        bill=1500 
        print(f"Adult tickets price are Rs.{bill}")

    wants_photo = input("Do you want to click the photo? Y or N. ")
    if wants_photo == "Y":
        bill += 300
        print(f"Your final bill is Rs.{bill}")
else:
    print("You Can`t ride the rollercoaster!")