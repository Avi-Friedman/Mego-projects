
# elaborate number is a number equal to the sum of its natural divisors
def an_elaborate_number(num):
    count = 0

    for i in range(1,num):
        if num % i == 0:
            count += i
    if count == num:
        print(f"the number {num} is elaborate number")
    else:
        print(f" the number {num} is not elaborate number")

for i in range(1,500):
    an_elaborate_number(i)