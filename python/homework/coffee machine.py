import coffee_machine_function
import coffee_machine_graphica


while coffee_machine_function.re == True:
    all_pay = 0
    print(coffee_machine_graphica.logo)
    add = "y"
    #Mode selection
    order = input("To order a drink, press enter!\n\n"
                      " press 'technician' for technician mode: ").casefold()
    if order!='' and order[0] == "t":
        #Entering a password and checking compatibility
        enter_password = int(input("pleas enter a password: "))
        if enter_password == coffee_machine_function.password:
            print("To print remaining components press 1.\n\n" 
                 "To print the cash register balance, press 2.\n\n" 
                   "To fill components press 3.\n\n")
            #Selecting technician options
            choosing_technician = int(input("Please enter your choice here: "))
            if choosing_technician == 1:
                print(coffee_machine_function.resources)
            elif choosing_technician == 2:
                print(coffee_machine_function.Cash_register)
            elif choosing_technician == 3:
                print("add water press 1.\n\n"
                      "add milk press 2.\n\n"
                      "add coffee press 3.")
                #Filling components
                adding_components = int(input("Please enter your choice here: "))
                if adding_components == 1:
                    coffee_machine_function.resources["water"] += int(input("Enter the amount of water you want to add: "))
                if adding_components == 2:
                    coffee_machine_function.resources["milk"] += int(input("Enter the amount of milk you want to add: "))
                if adding_components == 3:
                    coffee_machine_function.resources["coffee"] += int(input("Enter the amount of coffee you want to add: "))
                print(coffee_machine_function.resources)

    else:
        while add[0] == "y":

        #Add currency
            coin = input("pleas enter a coin. Penny(P)/Nickel(N)/Dime(D)/Quarter(Q)").casefold()
            #Calculation of value and accumulation
            pay = coffee_machine_function.value_coin[coin[0]]
            coffee_machine_function.Cash_register[coin[0]] += pay
            all_pay += pay
            coffee_machine_function.Cash_register["all_money"] += all_pay
            all_pay = float("{:.2f}".format(all_pay))
        #Option to add when the amount is not enough
            add = input(f"The amount you put in is: {all_pay}.\n\nWant to add currency?(yes/no)").casefold()

            if add[0] == "y":

                continue
            else:
                #Product selection
                 choice = input("please choose Latte / Cappuccino / Espresso: ").casefold()
                #A variable for a function reference
                 if choice[0] == "c":
                     choice_type = coffee_machine_function.cappuccino
                 if choice[0] == "e":
                     choice_type = coffee_machine_function.espresso
                 if choice[0] == "l":
                     choice_type = coffee_machine_function.latte

                #Check with the amount sufficient to purchase the product
                 if coffee_machine_function.Check_amount(all_pay, coffee_machine_function.price[choice[0]]) == False:

                    add = input("The amount you entered is not enough!!! \n\n Do you want to add coins?(y/n)")
                    if add[0] == "y":
                      continue
                    else:
                      break

                 else:
                    #Checking if the amount of components is sufficient for the selected product
                    if coffee_machine_function.resource_check(choice_type, coffee_machine_function.resources) == True:
                        print("I'm sorry but I can't prepare the drink you chose, try choosing something else")

                        continue
                    else:
                        coffee_machine_function.resource_check_cidrices(coffee_machine_function.resources, choice_type)
                       #Checking if there is an excess
                        if all_pay == coffee_machine_function.price[choice[0]]:
                            print("\n\ntake please your drink")
                        else:
                            #Checking if there is an excess
                            if coffee_machine_function.Cash_register["all_money"] > (all_pay - coffee_machine_function.price[choice[0]]):
                                print("\n\ntake please your drink\n\nDon't forget to take the excess!")
                            else:
                                print("\n\ntake please your drink\n\nWe are sorry but there is not enough excess on the device.")
