#תרגיל מס 1
def multiplicationTheNombers():
    result = 1
    for i in range (1, 4):
        number = int(input("pleese enter a number:"))
        result *= number
    print(f"The result is: {result}")

# תרגיל מס 2

def user_name_function():
    first_name = input("what is your first name?:")
    last_name = input("what is your last name?:")
    print("hello " + first_name +" " + last_name )

#תרגיל מס 3

def big_num_function():
    text = "the big number is: "
    first_num = int(input("pleese enter a number:"))
    sacend_num = int(input("pleese enter another num:"))
    third_num = int(input("Pleese enter a third number:"))
    if first_num > sacend_num and first_num > third_num:
        print(f"{text}{first_num}")
    elif sacend_num > first_num and sacend_num > third_num:
        print(f"{text}{sacend_num}")
    elif third_num > sacend_num and third_num > first_num:
        print(f"{text}{third_num}")
    else:
        print("No single large number found")

# תרגיל מס 4


def long_name_function():
    long_name = "No details entered"
    text = "The longest name is: "
    num = 0
    student_num = 0
    for i in range (1, 4):
        student_num = student_num + 1
        first_name = input(f" student num {student_num}: pleese enter your first nema: ")
        last_name = input(f" student num {student_num}: pleese enter your last nema: ")
        if len (first_name) + len (last_name) > num:
            num  = len (first_name) + len (last_name)
            long_name = first_name + " " + last_name
        elif len (first_name) + len (last_name) < num:
            long_name = long_name
        elif len (first_name) + len (last_name) == num:
            long_name = long_name + " and " + first_name + " " + last_name

    print(text + long_name)

# תרגיל מס 5

def even_function():
    num = int(input("pleese enter a number: "))
    if num % 2 == 0:
        print("the number is even!")
    else:
        print("the number isn't even!")

# תרגיל מס 6

import math
def area_function():
    radius = float(input("pleese enter a radius:"))
    s = float ("{:.2f}".format(radius * radius * math.pi))
    print(f"The area of the circle is: {s}")









