height = input("Enter your height in meter:- ")

weight = input("Enter your weight in kilogram:- ")

height_as_float = float(height)
weight_as_int = int(weight)

BMI = round(weight_as_int/height_as_float**2, 2)
if BMI<18.5:
    print(f"Your BMI is {BMI}, You are Under Weight")
elif BMI<25:
    print(f"Your BMI is {BMI}, You are Normal Weight")
elif BMI<30:
    print(f"Your BMI is {BMI}, You are Slightly overweight")
elif BMI<35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, You are clinically obese")
    