import hangmen_graphics
import random

fruit_list = ["apple", "cherry", "pear", "watermelon", "peach", "plum", "orange", "banana", "pineapple"]
the_chosen_fruit = random.choice(fruit_list)
num_for_chosen = len(the_chosen_fruit)
num_for_matches = 0 #ייצוג מספר למספר ההתאמות
num_for_list_graphics = 0 #מספור הדפסה ברשימת עץ
attempts = 7# מספר נסיונות שנשארו
letters = ["_"] * num_for_chosen
matches = "no"

print(hangmen_graphics.welcome)
input("--You have to discover the hidden fruit--\n\npleas enter to start")

while num_for_matches != num_for_chosen and attempts != 0:
    print(letters)
    player = input("please enter a letter: ").casefold()

    for i in range (num_for_chosen + 1):

        if letters[i-1] != player:

            if player == the_chosen_fruit[i-1]:
                matches = "yes" # פרמטר לזיהוי אם יש התאמה בסיום הלולאה
                letters[i-1] = player
                num_for_matches += 1

                break
            else:
                matches = "no"
                continue
        elif letters[i-1] == player:
            continue

    if matches == "yes":
        continue

    elif matches == "no":
        print(hangmen_graphics.HANGMANPICS[num_for_list_graphics])
        num_for_list_graphics += 1
        attempts -= 1
        print(f"You have {attempts} attempts left")

if attempts == 0:
    print("\n\nThe chosen fruit is: " + the_chosen_fruit)
    print("\n\nyou are loser\n\n" + hangmen_graphics.gema_over)

elif num_for_matches == num_for_chosen:
    print(letters)
    print("\n\nyou did well\n\n" + hangmen_graphics.win)











