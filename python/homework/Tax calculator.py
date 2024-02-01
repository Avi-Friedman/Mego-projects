# tax_percent = 0
# monthly_salary_1 = int(input("Please enter your monthly salary:"))
# monthly_salary = monthly_salary_1
# pay = 0
#
# for monthly_salary in range(monthly_salary, 0, -1):
#     if monthly_salary < 7011:
#         tax_percent = 0.10
#     elif 7010 < monthly_salary < 10061:
#         tax_percent = 0.14
#     elif 10060 < monthly_salary < 16151:
#         tax_percent = 0.20
#     elif 16150 < monthly_salary < 22441:
#         tax_percent = 0.31
#     elif 22440 < monthly_salary < 46691:
#         tax_percent = 0.35
#     elif 46690 < monthly_salary < 60131:
#         tax_percent = 0.47
#     elif monthly_salary > 60130:
#         tax_percent = 0.50
#     pay += 1 * tax_percent
#
# print("The amount of tax you are required to pay is: %.2f  Your monthly income after tax deduction is: %.2f"%(pay, monthly_salary_1 - pay))
#
# pay_2 = 0
# monthly_salary_2 = int(input("enter your:"))
# if monthly_salary_2 < 7011:
#     pay_2 = monthly_salary_2 * 0.10
# elif 7010 < monthly_salary_2 < 10061:
#     pay_2 = ((monthly_salary_2 - 7010) * 0.14) + 701
# elif 10060 < monthly_salary_2 < 16151:
#     pay_2 = ((monthly_salary_2 - 10060) * 0.20) + 427 + 701
# elif 16150 < monthly_salary_2 < 22441:
#     pay_2 = ((monthly_salary_2 - 16150) * 0.31) + 1218 + 427 + 701
# elif 22440 < monthly_salary_2 < 46691:
#     pay_2 = ((monthly_salary_2 - 22440) * 0.35) + 1949.9 + 1218 + 427 + 701
# elif 46690 < monthly_salary_2 < 60131:
#     pay_2 = ((monthly_salary_2 - 46690) * 0.47) + 8487.5 + 1949.9 + 1218 + 427 + 701
# elif monthly_salary_2 > 60130:
#     pay_2 = ((monthly_salary_2 - 60130) * 0.50) + 6316.8 + 8487.5 + 1949.9 + 1218 + 427 + 701

# print(f" the pay tax is {pay_2}!!!")

monthly_salary = int(input("enter:"))
tax_brackets = [0, 7010, 10060, 16150, 22440, 46690, 60130]
tax_percent =[0, 0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5]
pay = 0
i = 1
while i < 7 and monthly_salary > tax_brackets[i]:
    pay += (tax_brackets[i] - tax_brackets[i-1]) * tax_percent[i]
    i += 1
pay += (monthly_salary - tax_brackets[i-1]) * tax_percent[i]
print("The amount of tax you are required to pay is: %.2f  Your monthly income after tax deduction is: %.2f"%(pay, monthly_salary - pay))
