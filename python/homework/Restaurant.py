age = float(input("plese, enter your age:"))
height = float(input("plese enter your height(in cm):"))
cars_ticket = 25
cars_ticket_18 = 20
anaconda_ticket = 30
if age >= 12:
    pic = input("Do you want to take a picture? (the price is: 5 ILS)answer \"yes\" or \"no\":")
    if pic == "yes":
        cars_ticket += 5
        anaconda_ticket += 5
        cars_ticket_18 += 5
    else:
        cars_ticket = 25
        anaconda_ticket = 30
        cars_ticket_18 = 20
    if age < 18:
        if height >=150:
             print(f"Welcome to the Anaconda! the price for ticket is: {anaconda_ticket_18} ILS")
        else:
            print(f"Your comment will not be able to enter Anaconda!\n You can get into colliding cars.\n You are entitled to a benefit. the price for ticket is only: {cars_ticket} ILS")
    else:
        print(f"Your comment will not be able to enter Anaconda!\n You can get into colliding cars.\n the price for ticket is: {cars_ticket} ILS")

elif height >=150:
    print("You can't enter the amusement park.\n You are welcome to visit the zoo down the street.")
else:
    print("You can't enter the amusement park. You are welcome to visit the zoo down the street.\n You are entitled to an entry ticket at 10 ILS.")