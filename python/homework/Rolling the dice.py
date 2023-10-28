import random
dice_1 = random.randint(1, 6)
user_random_1 = input(f"The number assigned by the computer is: {dice_1}\n Please press enter to roll a die_")
user_random_1 = random.randint(1, 6)
print(f"The number you got is: {user_random_1}")
dice_2 = random.randint(1, 6)
user_random_2 = input(f"The number assigned by the computer is: {dice_2}\nPlease press enter to roll another die_")
print(f"The number you got is: {user_random_2}")
user_random_2 = random.randint(1, 6)
print(f"The number you got is: {user_random_2}")
sum_random = dice_1 + dice_2
sum_user = user_random_1 + user_random_2
resolt = f"Your amount is: {sum_user}. and the computer's amount is: {sum_random}.\n"
if sum_random > sum_user:
    print(f"{resolt}You are the loser!!!")
elif sum_random < sum_user:
    print(f"{resolt}you are the winner!!!")
else:
    print(f"{resolt}There is no winner!!!")