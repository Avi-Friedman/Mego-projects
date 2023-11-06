import limperial_graphics
import os
def code(text, offset):
    for i in range(len(text)):

        num = ord(text[i]) + offset
        if num > 122:
            num = num - 26
        elif num < 97:
            num = num + 26

        new_text[i] = (chr(num))

print(limperial_graphics.logo)
additional = "yes".casefold()
while additional[0] == "y":
    user_choice = int(input("Choose what would you like to do:\n\nEncrypt (press 1)"
                            "\n\ndecrypt (press 2)"))
    user_text = input("pleas enter the word you want to encrypt: ").casefold()
    user_offset = int(input("pleas enter your offset: "))
    new_text = [''] * len(user_text)
    if user_choice == 1:
        user_offset = user_offset
    elif user_choice == 2:
        user_offset = (user_offset * (-1))

    code(user_text, user_offset)

    print(''.join(new_text))

    additional = input("Do you want to decrypt/encrypt something else?(yes/no): ")

    if additional == "y":

        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Thank you for using our services!")
















