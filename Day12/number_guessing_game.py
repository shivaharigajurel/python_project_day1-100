import random
from art import logo
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess>answer:
        print("Too high. ")
        return turns-1
    elif guess <answer:
        print("Too Low. ")
        return turns-1
    elif guess == answer:
        print(f"You get it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        global turns
        return EASY_LEVEL_TURNS
        

    elif level == "hard":
         return HARD_LEVEL_TURNS
    


os.system('cls')


def game():
    print(logo)
    answer = random.randint(0,100)
    print(F"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {answer}")
    turns = set_difficulty()


    guess= 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns ==0:
            print("You've ran out guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()





