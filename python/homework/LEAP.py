year = int(input("plese enter year:"))
leap = ("Teh year is LEAP")
no_leap = ("The year is not LEAP")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap)
        else:
            print(no_leap)
    else:
        print(leap)
else:
    print(no_leap)



