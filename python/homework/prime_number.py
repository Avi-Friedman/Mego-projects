def function():
    count = 0
    for i in range (2, num):
        if num % i == 0:
            count = count + 1
        else:
            count = count
    if count > 0:
        print("the number is not prime")
    else:
        print("the number is prime")

num = int(input("pleese enter a number: "))

function()

#for num in range (1, 101): בדיקה עם נתוכנית עובדת
   # print(num)

    #function()





