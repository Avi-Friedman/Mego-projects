import random

#A function to reduce the number of attempts:
def reduction(a):
    a -= 1
    return a

#Function to check with the number is greater, less or equal:
def examination(a, b):
    if a > b:
        return "big"
    elif a < b:
        return "small"
    elif a == b:
        return "equal"

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






