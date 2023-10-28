import graphics
import random
play_list = [graphics.rock, graphics.paper, graphics.pcissors]
player_choice = int(input("please choice: rock = 0, paper = 1, scissors = 2."))
computer_choice = random.randint(0,2)
print(f"The computer chose: {play_list[computer_choice]} \n and you chose: {play_list[player_choice]}")
if player_choice == computer_choice:
    print("There is no winner")
elif (player_choice + computer_choice)%2 == 0:
    if player_choice < computer_choice:
        print("you are the winner!!")
    else:
        print("you are the loser!!")
else:
    if player_choice > computer_choice:
        print("you are the winner!!")
    else:
        print("you are the loser!!")