import math
def amount_of_cans(length, width):
     num_cans = length * width / 5
     print(f"you need {math.ceil(num_cans)} amount of cans")

length = float (input("plese enter length: "))
width = float (input("pleese ente width: "))

amount_of_cans(length, width)






