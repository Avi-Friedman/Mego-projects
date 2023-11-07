import The_guessing_game_graphic
import The_guessing_game_global_variables

level = "a"
attempts = 0

print(The_guessing_game_graphic.logo)

print("Welcome to the guessing game!\n\n")

while level[0] != "h" and level[0] != "e":

    level = input(f"choose difficulty: type 'easy' or 'hard': ").casefold()
    if level[0] != "h" and level[0] != "e":
        print(f"Your selection is invalid.")
        continue

    elif level[0] == "h":
        attempts = The_guessing_game_global_variables.hard

    elif level[0] == "e":
        attempts = The_guessing_game_global_variables.easy


while attempts != 0:
    user_num = int(input("pleas enter a number between 1 to 100: "))

    if The_guessing_game_global_variables.number_legality(user_num) == "agine":
        print("The number is out of range")
        continue

    elif The_guessing_game_global_variables.examination(user_num, The_guessing_game_global_variables.computer_num) == "big":
        attempts = The_guessing_game_global_variables.reduction(attempts)
        print(f"The number you chose is too big {The_guessing_game_global_variables.attempts_text}{attempts}")

    elif The_guessing_game_global_variables.examination(user_num, The_guessing_game_global_variables.computer_num) == "small":
        attempts = The_guessing_game_global_variables.reduction(attempts)
        print(f"The number you chose is too small {The_guessing_game_global_variables.attempts_text}{attempts}")

    else:
        break

if attempts == 0:
    print(f"\n\nYou failed to guess the correct number.\n\n The selected number is: {The_guessing_game_global_variables.computer_num}\n\n{The_guessing_game_graphic.loser}")

else:
    print(f"\n\nYou guessed the right number!!!\n\n{The_guessing_game_graphic.win}")


