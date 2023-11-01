height = input("Enter your height in meter:- ")

weight = input("Enter your weight in kilogram:- ")

height_as_float = float(height)
weight_as_int = int(weight)

BMI = str(weight_as_int/height_as_float**2)

print("Your body mass index is "+ BMI)