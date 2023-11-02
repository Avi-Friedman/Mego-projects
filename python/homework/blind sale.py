import os


another = "yes"
proposal_1 = 0
name_1 = "a"

while (another[0]) == "y":
    name = input("plesse enter your name: ")
    proposal = int(input("pleese enter your proposal: "))
    another = input("is there another suggestion? ").casefold()
    if (another[0]) == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    if proposal > proposal_1:
        proposal_1 = proposal
        name_1 = name
    else:
        proposal = proposal_1
        name = name_1
print(f"the higher is: {proposal}, and the winner us: {name}")













