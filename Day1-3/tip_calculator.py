print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill RS. "))


tip = int(input("What persentage Would you like to give? 10, 12 or 15? "))

total_tip = total_bill*tip/100
with_tip = total_bill + total_tip


number_of_people = int(input("How many people split the bill? "))

one_person_pay = with_tip/number_of_people

final_ammount = "{:.2f}".format(one_person_pay)

print(f"Each person should pay: Rs. {final_ammount}")
