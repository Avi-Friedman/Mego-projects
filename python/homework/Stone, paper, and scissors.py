import random
import grafica
play_list = [grafica.stone, grafica.paper, grafica.scissors]
computer_choice = (play_list[random.randint(0, 2)])
user_choice = int(input("plese choice (stone = 0, paper = 1, scissors =2):"))
user_choice = play_list[user_choice]
resolt = (f"The computer choose: {computer_choice}.\n and you choose: {user_choice}")
user_win = "you are the winner!!!"
computer_win = "you are the loser!!!"
draw = "There is no winner!!!"
if computer_choice == (play_list[0]):
    if user_choice == (play_list[1]):
        print(f"{resolt}\n\n{user_win}")
    elif user_choice == (play_list[2]):
         print(f"{resolt}\n\n{computer_win}")
    else:
        print(f"{resolt}\n\n{draw}")
elif computer_choice == (play_list[1]):
    if user_choice == (play_list[0]):
        print(f"{resolt}\n\n{computer_win}")
    elif user_choice == (play_list[2]):
        print(f"{resolt}\n\n{user_win}")
    else:
        print(f"{resolt}\n\n{draw}")
elif computer_choice == (play_list[2]):
    if user_choice == (play_list[0]):
        print(f"{resolt}\n\n{user_win}")
    elif user_choice == (play_list[1]):
        print(f"{resolt}\n\n{computer_win}")
    else:
        print(f"{resolt}\n\n{draw}")

