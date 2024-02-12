# num = int(input("enter number:"))
# num_2 = int(input("enter outher number:"))
# def multiple(a, b):
#     result = 0
#     for i in range(b):
#         result += a
#     # print(f"the result {a} * {b} is: {result}")
#     return result
# #
# def division(a, b):
#     result = a
#     while multiple(result, result) != a:
#         result -= 1
#     print(f"the result {a} // {b} is: {result}")
#
# def square_root(a):
#     result = 1
#     while multiple(result, result) != a:
#         result += 1
#     print(f"the Square root for {a} is: {result}")
#
# num = int(input("enter num: "))
# all = num % 10 + (num % 100 // 10) + num // 100
# num_for_one = all // 3
# rest = all % 3
# print(f"{all}\n{num_for_one}\n{rest}")
# if all % 3:
#     print (True)
# else:
#     print(False)

# from datetime import datetime
# now = datetime.now()
# print(f"{now:%d/%m/%y %H:%M:%S}")
# a = "He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3)
# print(a)
# user_string = input("please enter your string: ")
# new_string = user_string[:len(user_string)//2].lower()+ user_string[len(user_string)//2::].upper()
# print(new_string)
# my_string = "my name is avi friedman i'm a 38 years old."
# print(my_string.zfill())

def charecter_in_tuple(tuple, a):
    for item in tuple:
        if a in item:
            return True
    return False
def all_charecter(tuple):
    for i in range(97, 123):
        if charecter_in_tuple(tuple, chr(i)):
            print(chr(i))
            if i == 122:
                return True
        else:
                return False

# a= input()
word = ("abcde", "fghijklmnop", "qrstuvwxyz")
print(all_charecter(word))
a, b, c = word
print(b)
my_list = list(word)
my_list = tuple(my_list)
print(my_list)