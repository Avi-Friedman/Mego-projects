import random
import grafica
next = "To continue press \"Enter\""
name = input("welcome to the master play!!!\nplese enter yout name:")
print("Hello " + name +
" You open your eyes and find yourself lying on the ground with treetops towering high above you.\n"
"In the first moment you do not understand what is happening to you and how you got to the place\n "
"and the situation you are in and then you remember\n\n"
"that in the morning you were on a plane when the pilot announced an engine failure \n"
"and since then you don't remember anything.\n"
"Dangers and adventures lie in wait for you \n"
"along the way and you must be smart enough to make brave and wise decisions.\n"
"You rub your aching bones and get up thinking and debating whether to move\n"
" forward on the path to your right north or south\n\n ")
for i in range(1, 4):

    direction_of_progress = (input("what do you choose to do? 'North' or 'South'?"))
    direction_of_progress = direction_of_progress.casefold()[0]

    if  direction_of_progress == "n":
        print("Excellent choice!!!\n\n You shortened the path significantly.\n\n")
        print("You continue on the road and suddenly.\n "
                     "you hear the sound of a goat bleating in supplication.\n"
                     " You look in the direction and see a wounded goat.\n "
                     "It is obvious that she was attacked by a pack of wolves.\n\n")
        help = input(" Will you come over to help or continue on your way? (Answer 'Yes' or 'No')").casefold()[0]
        if help == "n":
            print("Excellent choice!!!\n\n The goat's injury indicates that the place is infested with predators.\n\n"
                  " You saved your life!!!\n\n")
            input(next)
            enter = input(f"You advance on your way exhausted,\n"
                          " tired and hungry and suddenly you see a cabin in the middle of the forest.\n\n"
                      "You pinch yourself, make sure it's not a mirage. But the reality surpasses all imagination.\n"
                   f"You approach... the cabin is suspicious in your eyes... you hesitate whether to enter.\n{grafica.hut}"
                    "To log in, write \"Enter\" and if you don't want to log in, write \"Continue\":\n\n")
            enter = enter.casefold()[0]
            if enter == "e":
                swith = input("You enter... you are inside... the place is dark and neglected.\n\n "
                              "You see a switch on the wall.\n\n "
                              "You think it's used to turn on the light but it looks a little suspicious to you.\n\n"
                              "Would you like to press the switch? (Yes or No?)")
                swith=swith.casefold()[0]

                if swith == "n":
                    stairs = input("You grope in the dark and find a flight of stairs.\n\n "
                                   "Would you like to go down the stairs or into an adjacent room? (\"Yes\" or \"No\")")
                    stairs = stairs.casefold()[0]
                    if stairs == "n":
                        print(f"You managed to get out of the forest safely!!!\n\n{grafica.good_job}{grafica.game_over}")
                        break
                    elif stairs == "y":
                        print("Oops... you've been captured by the forest monster." + grafica.monster+"\n\n "
                              "The monster has a weakness to 'stone paper and scissors'.\n\n "
                              "You can face it.\n\n If you win you will receive your life as a gift!!!\n\n")
                        input(next)
                        play_list = [grafica.stone, grafica.paper, grafica.scissors]
                        computer_choice = (play_list[random.randint(0, 2)])
                        user_choice = int(input("plese choice (stone = 0, paper = 1, scissors =2):\n\n"))
                        user_choice = play_list[user_choice]
                        resolt = (f"The computer choose: {computer_choice}.\n and you choose: {user_choice}")
                        user_win = "you are the winner!!!"
                        The_monster_win = "you are the loser!!!"
                        draw = "There is no winner!!!"
                        saved = "You received your soul as a booty.\n\n " \
                                "The monster reveals to you that in the room above there is food and a map,\n" \
                                " with which you can rescue yourself.\n\n " \
                                "You go up to the room, take the map and the food and manage to save yourself."
                        if computer_choice == (play_list[0]):
                            if user_choice == (play_list[1]):
                                print(f"{resolt}\n\n{user_win}\n\n{saved}\n\n\n{grafica.good_job}\n\n{grafica.game_over}")
                                break
                            elif user_choice == (play_list[2]):
                                print(f"{resolt}\n\n{The_monster_win}\n\n\n{grafica.game_over}")
                                break
                            else:
                                print(f"{resolt}\n\n{draw}\n\n{saved}\n\n\n{grafica.game_over}")
                                break
                        elif computer_choice == (play_list[1]):
                            if user_choice == (play_list[0]):
                                print(f"{resolt}\n\n{The_monster_win}\n\n\n{grafica.game_over}")
                                break
                            elif user_choice == (play_list[2]):
                                print(f"{resolt}\n\n{user_win}\n\n{saved}\n\n\n{grafica.good_job}\n\n{grafica.game_over}")
                                break
                            else:
                                print(f"{resolt}\n\n{draw}\n\n{saved}\n\n\n{grafica.game_over}")
                                break
                        elif computer_choice == (play_list[2]):
                            if user_choice == (play_list[0]):
                                print(f"{resolt}\n\n{user_win}\n\n{saved}\n\n\n{grafica.good_job}\n\n{grafica.game_over}")
                                break
                            elif user_choice == (play_list[1]):
                                print(f"{resolt}\n\n{The_monster_win}\n\n\n{grafica.game_over}")
                                break
                            else:
                                print(f"{resolt}\n\n{draw}\n\n{saved}\n\n\n{grafica.game_over}")
                                break
                elif swith == "y":
                    print("The switch activated a bomb that blew up the cabin with everyone in it.\n\n" +  grafica.game_over)
                    break
            elif enter == "c":
                print("You lose your way and find yourself at the starting point.\n\n")
                continue
        elif help == "y":
            print("You lingered there and served as dinner for a pack of wolves." + grafica.wolv +"\n\n\n" + grafica.game_over)
            break
    elif direction_of_progress == "s":
        sleep = input("You are moving forward and the day is getting dark,\n\n you need to get ready for the night."
                      "\n\n Will you choose to climb a tree and sleep on a wide branch "
                      "\nor do you prefer to stay overnight on the ground? (Answer 'ground' or 'tree')\n\n")
        sleep = sleep.casefold()[0]
        if sleep == "t":
            morning = input("The morning has dawned and you wake up to the sound of birds chirping.\n"
                  " You plan to climb down from the tree but notice that the branch you used to climb has broken.\n\n"
                  " You can try to jump or alternatively slide on the trunk of the tree and risk bruises from branches.\n\n"
                  " (for jumping it says 'Jump' and for sliding it says 'Slide'):\n\n")
            morning = morning.casefold()[0]
            if morning == "s":
                food = input("You got off the tree. \n"
                             "Although you are bruised and bleeding, you are fit to continue the journey.\n "
                             "You keep walking and your stomach reminds you of her existence.\n"
                             " You remember that you haven't had any food in your mouth for over a day.\n"
                             " You are looking for something to satisfy your hunger \n"
                             "and you catch sight of mushrooms growing on the side of the road, \n"
                             "some white and some red.\n\n"
                             " Which one will you choose to eat? (insert 'Red' and 'White'):")
                food=food.casefold()[0]
                if food == "w":
                          print("You ate... \n"
                                "you gained strength and you can continue.\n"
                                " You move forward and hear the noise of a helicopter.\n"
                                " These are the rescue forces looking for survivors of the crash.\n"
                                " You wave for help over and over again until you get their attention and they take you back to your house..\n\n\n"
                                + grafica.good_job + "\n\n"+ grafica.game_over)
                          break
                elif food == "r":
                    print("The mushrooms you ate are poisonous.\n\n you're dead." + grafica.game_over)
                    break
            elif morning == "j":
                print("Thought you were Rambo?\n\n You broke your legs,\n\n you can't move forward!\n\n\n" + grafica.game_over)
                break
        elif sleep == "g":
            print("You stayed to sleep on the ground and became food for prey animals.\n\n\n" + grafica.wolv + grafica.game_over)
            break





