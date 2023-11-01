import random

letters = ['a', 'b', 'A', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '}', '~']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letter would you like on your password?\n"))
nr_symbools = int(input("How many symbool would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# easy

# password = ""
# for char in range(1, nr_letters+1):
#     password += random.choice(letters)

# for char in range(1, nr_symbools+1) :
#     password += random.choice(symbols)

# for char in range(1, nr_numbers+1)  :
#     password += random.choice(numbers)

# print(password)


# Hard
password_list = []
for char in range(1, nr_letters+1):
    password_list += random.choice(letters)

for char in range(1, nr_symbools+1) :
    password_list += random.choice(symbols)

for char in range(1, nr_numbers+1)  :
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


