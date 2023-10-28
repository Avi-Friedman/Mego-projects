age = float(input("plese enter your age:"))
height = float(input("plese enter your(in meter):"))
weight = float(input("plese enter yout weight (in KG):"))
bmi_ = weight / (height * height)
bmi = float("{:.2f}".format(bmi_))
if age < 65:
    if bmi < 18.5:
        print(f"your BMI is: {bmi} you are underweight! You should go get checked.")
    elif bmi < 25:
        print(f"your BMI is: {bmi} your weight is excellent. Keep taking care of yourself!")
    elif bmi < 30:
        print(f"your BMI is: {bmi} your weight is higher than average!")
    else:
        print(f"your BMI is: {bmi} you are obese! Go take care of it.")
elif age <= 74:
    if bmi < 22:
        print(f"your BMI is: {bmi} you are underweight! You should go get checked.")
    elif bmi < 27:
        print(f"your BMI is: {bmi} your weight is excellent. Keep taking care of yourself!")
    elif bmi < 30:
        print(f"your BMI is: {bmi} your weight is higher than average!")
    else:
        print(f"your BMI is: {bmi} you are obese! Go take care of it.")
else:
    if bmi <= 23:
        print(f"your BMI is: {bmi} you are underweight! You should go get checked.")
    elif bmi < 28:
        print(f"your BMI is: {bmi} your weight is excellent. Keep taking care of yourself!")
    elif bmi < 30:
        print(f"your BMI is: {bmi} your weight is higher than average!")
    else:
        print(f"your BMI is: {bmi} you are obese! Go take care of it.")
