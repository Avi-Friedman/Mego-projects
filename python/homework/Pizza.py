
name = input("wellcome to The PIZZA\n What is your name?:")
size = input(f"Hello {name} plese choose size: Large, Medium or Small: ")
size = size.casefold()     #הפונקציה ממירה טקסטים שנכתבו באןתיות גדולות לאותיות קטנות
koren = input("do you want add Koren? ").casefold()
mushroom = input("do you want add Mushroom? ").casefold()
cheese = input("do you want add cheese? ").casefold()
price = 0
if size == "large":
    price += 25
    if koren == "yes":
        price += 6
    if mushroom == "yes":
        price += 5
elif size == "medium":
    price += 20
    if koren == "yes":
        price += 4
    if mushroom == "yes":
        price += 5
elif size == "small":
    price += 15
    if koren == "yes":
        price += 2
    if mushroom == "yes":
        price += 2
if cheese == "yes":
    print("ya batata!!!!!")
    price += 3
else:
    print("The size not found.\n plese choose size!")# הפלט שיודפס במקרה ויוזן גודל שאינו מופיע באפשרויות
print(f"The amount to be paid is: {price} ILS")







#x = txt.casefold()
