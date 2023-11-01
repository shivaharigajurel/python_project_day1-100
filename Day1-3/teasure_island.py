print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")

print('You`re at a cross road. Where do you want to go? Type "left" or "right". ')
side = input().lower()

if side=="left":
    print('You come to a lake. There is an island in the middle of the lake type "wait" to wait for a boat. Type "swim" to swim across. ')
    choice = input().lower()
    if choice == "wait":
        print('You arrive at the island unharmed. There is house with three doors. "red", "blue" and "yellow". Which colour do you choose?')
        choose_colour = input().lower()
        if choose_colour == "yellow":
            print("You found the treasure! You Win!")
        elif choose_colour == "blue":
            print("You enter a room of beasts. Game Over")
        elif choose_colour == "red":
            print("Its a room full of fire. Game over.")
        else:
            print("The door doesn`t exists. Game Over")

    else:
        print("You attacked by an angry trout. Game Over.")
        
else:
    print("You fell into a hole. Game Over.")
