# names = names_string.split(",")

import random
names = ["Ram", "Shyam", "Hari", "Sita"]
num_items =len(names)
random_choice =random.randint(0, num_items-1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay+" is going to buy meal today")
