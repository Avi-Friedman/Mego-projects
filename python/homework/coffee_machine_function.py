import os
espresso= {
    "water": 50,
    "milk": 0,
    "coffee": 18,
    "cost": 1.5
    }

latte= {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
}

cappuccino= {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
value_coin = {"p": 0.01,
                "n": 0.05,
                "d": 0.1,
                "q": 0.25}

Cash_register =  {"p": 0,
                "n": 0,
                "d": 0,
                "q": 0,
                "all_money": 2.5}

price = {
    "e": 1.5,
    "l": 2.5,
    "c": 3.0

}
password = 1234
short = 0
re = True
i = 0

#A function to check if there are components in stock
def resource_check(lat, res):
    short = 0
    my_list = ["water", "milk", "coffee"]
    for i in range (3):

        component = my_list[i]
        if lat[component] > res[component]:
            short = 1
        else:
            continue
    if short == 1:
        return True
    else:
        return False

#A function to check if the money is enough for the selected product
def Check_amount(us_m, cho):
    if us_m < cho:
        return False
    else:
        return True

def resource_check_cidrices(res, lat):

    my_list = ["water", "milk", "coffee"]
    for i in range (3):

        component = my_list[i]
        res[component] -= lat[component]

        return res






