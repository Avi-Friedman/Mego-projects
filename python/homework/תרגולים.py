def multiplae(num_1, num_2):
    result = num_1*num_2
    print(result)

def division(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        result = "the action not legal"
    else:
        result = num_1 / num_2
    return result

user_num_1 = int(input("please enter a number: "))
user_num_2 = int(input("please enter a number: "))
sum = division(user_num_1, user_num_2)
print("the result for division {0} and {1} is {2}".format(user_num_1, user_num_2, sum))
print(f"the result for division {user_num_1} and {user_num_2} is {sum}")
print("the result for division %d and %d is %.1f" % (user_num_1, user_num_2, sum))



