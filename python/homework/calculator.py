def addition(a, b):
    return a + b

def division(a, b):
    return a / b

def subtraction(a, b):
    return a - b

def multiplication(a, b,):
    return a * b


user_num_1 = int(input("pleas enter a first number: "))
type_of_action = input("pleas enter what do you wont to do: addition(+), subtraction(-), multiplication(*), division(/): ").casefold()
user_num_2 = int(input("pleas enter another number: "))
if type_of_action == "+" or type_of_action[0] == "a":
    result = addition(user_num_1, user_num_2)
elif type_of_action == "-" or type_of_action[0] == "s":
    result = subtraction(user_num_1, user_num_2)
elif type_of_action == "*" or type_of_action[0] == "m":
    result = multiplication(user_num_1, user_num_2)
elif type_of_action == "/" or type_of_action[0] == "d":
    result = division(user_num_1, user_num_2)
print(f"the result of {user_num_1} {type_of_action} {user_num_2} is: {result}")


