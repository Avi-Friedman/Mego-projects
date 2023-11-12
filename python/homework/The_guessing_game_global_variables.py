import random

#A function to reduce the number of attempts:

attempts = 0
#Function to check with the number is greater, less or equal:
def examination(a, b, c):

    if a == b:
        print(f"\n\nYou guessed the right number!!!\n\n{The_guessing_game_graphic.win}")

        return
    if a > b:
        print(f"The number you chose is 'too big' {attempts_text}{attempts}")
        if attempts == 0:
            print( f"\n\nYou failed to guess the correct number.\n\n The selected number is: {The_guessing_game_global_variables.computer_num}\n\n{The_guessing_game_graphic.loser}")
    else:
        print(f"The number you chose is 'too small' {attempts_text}{attempts}")
        if attempts == 0:
            print(f"\n\nYou guessed the right number!!!\n\n{The_guessing_game_graphic.win}")

    return c -1
#A function to check that the number entered by the user is within the legal range:
def number_legality(a):
    if a > max or a < min:
        return "agine"


hard = 5
easy = 10
#Variable to select a number by the computer
computer_num = random.randint(1, 100)
max = 100
min = 1
attempts_text = "The number of attempts left is: "






