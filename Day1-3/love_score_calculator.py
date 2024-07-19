print("The Love Calculator is Calculating your score . . . . . \n\n")

name1 = input("Enter Your name:- ")
print("\n")
name2 = input("Input your Lover name:- ")
print("\n")


combined_names = name1+name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l+o+v+e

if combined_names :
    score = 100
else:
    score = int(str(first_digit)+str(second_digit))

if score<10 or score>90:
    print(f"Your score is {score}, You together like coke and mentos. ")
    print("\n\n")
elif score>=40 and score<=50:
    print(f"Your Score is {score}, You alright together. ")
    print("\n\n")
else:
    print(f"Your love score is {score}")
    print("\n\n")