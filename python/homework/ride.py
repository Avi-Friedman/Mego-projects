print("good morning " + input("plese enter your name:"))
height = float(input("plese enter your height (in cm):"))
if height > 120:
    print("what fun!!! you can ride")
    age = float(input("plese enter yout age:"))
    if age < 12:
        print("To be paid: 5$")
    elif age < 18:
        print("To be paid: 7$")
    else:
        print("To be paid: 12$")
else:
    ("sori!! you can't ride")


