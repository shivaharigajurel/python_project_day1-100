import random
import hangman_stages
import word_list


chosen_word =random.choice(word_list.word_list)
print(hangman_stages.logo)

display = []
word_lenth = len(chosen_word)
for _ in range(word_lenth):
    display += "_"

lives = 6
   

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Input a letter: ").lower()

    if guess in display:
        print(f"You`ve already guessed {guess}")



    for position in range(word_lenth):
        letters = chosen_word[position]
        if letters == guess:
            display[position] =letters

    if guess not in chosen_word:
        print(f"You guessed {guess} ,that`s not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(hangman_stages.stages[lives])
    




