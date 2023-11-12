import The_guessing_game_graphic
import random

level = "a"
attempts = 0
hard = 5
easy = 10
#Variable to select a number by the computer
computer_num = random.randint(1, 100)
max = 100
min = 1
attempts_text = "The number of attempts left is: "

def examination(a, b, c):

    if a == b:
        print(f"\n\nYou guessed the right number!!!\n\n{The_guessing_game_graphic.win}")
        return
    if a > b:
        print(f"The number you chose is 'too big' {attempts_text}{attempts}")
    else:
        print(f"The number you chose is 'too small' {attempts_text}{attempts}")
    if c == 0:
        print(f"\n\nYou failed to guess the correct number.\n\n The selected number is:"
              f" {computer_num}\n\n{The_guessing_game_graphic.loser}")


def number_legality(a):
    if a > max or a < min:
        return "agine"


print(The_guessing_game_graphic.logo)

print("Welcome to the guessing game!\n\n")

while level[0] != "h" and level[0] != "e":
#Choose a difficulty level
    level = input(f"choose difficulty: type 'easy' or 'hard': ").casefold()
    #Check if the selection is valid
    if level[0] != "h" and level[0] != "e":
        print(f"Your selection is invalid.")
        continue

    elif level[0] == "h":
        attempts = hard

    elif level[0] == "e":
        attempts = easy
num = attempts
for i in range(num):
    user_num = int(input("pleas enter a number between 1 to 100: "))
    #A reference to a function that checks if the number is within the legal range
    if number_legality(user_num) == "agine":
        print("The number is out of range")
        continue
    attempts -= 1
    #A reference to a function that checks if the number is greater, less or equal
    examination(user_num, computer_num, attempts)




