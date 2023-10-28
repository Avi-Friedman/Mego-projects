'''name = print("Good morning!" (input("What is your name? "))
print("Hello" + name)
weight = float(input("plese enter your weight: "))
height = float(input("plese enter your height:"))
bmi = (weight / (height * height))
print("your bmi is" + str(bmi))'''

num = input (int("plese enter nuber"))





name = input("wellcome to The PIZZA\n What is your name?:")
size = input(f"Hello {name} plese choose size: Large, Medium or Small: ")
size = size.casefold()
price = 0
#if size == large or medium or small:
if size == "large":
    price += 25
    koren = input("do you want add Koren? ").casefold()
    if koren == "yes":
        price += 6
   #else:
    #    price +=0
    mushroom = input("do you want add Mushroom? ").casefold()
    if mushroom == "yes":
        price += 5
    #else:
     #   price +=0

elif size == "medium":
    price += 20
    koren = input("do you want add Koren? ").casefold()
    if koren == "yes":
        price += 4
   # else:
    #    price += 0
    mushroom = input("do you want add Mushroom? ").casefold()
    if mushroom == "yes":
        price += 5
    #else:
     #   price += 0
elif size == "small":
    price += 15
    koren = input("do you want add Koren? ").casefold()
    if koren == "yes":
        price += 2
   # else:
    #    price += 0
    mushroom = input("do you want add Mushroom? ").casefold()
    if mushroom == "yes":
        price += 2
    #else:
     #   price += 0
    cheese = input("do you want add cheese? ").casefold()
    if cheese == "yes":
        print("ya batata")
        price += 3


else:
    print("The size not found.\n plese choose size!")
print(f"The amount to be paid is: {price}")







#x = txt.casefold()


