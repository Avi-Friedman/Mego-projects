from turtle import Turtle, Screen
import random



def chackWin(a,b,c):
    if a >= 225:
        if b == c:
            return True
        else:
            return False
    else:
        return None

new_list = []
screen = Screen()
screen.setup(width=500, height=400)


colors = ["red", "blue", "orange", "purple", "green"]
y_positions = [-50, -10, 30, 70, 110]

for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.speed(1)
    tim.goto(x=-230, y=y_positions[i])
    new_list.append(tim)
the_winning_turtle = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (enter a color): ")
print(f"your choice: {the_winning_turtle}")
game = True
while game == True:
    for item in new_list:
        step = random.randint(1, 25)
        item.forward(step)
        if chackWin(item.xcor(), item.pencolor(), the_winning_turtle) == None:
            continue


        elif chackWin(item.xcor(), item.pencolor(), the_winning_turtle) == True:
            print("Your bet was successful!!! You scooped up the entire pot.")
            game = False
            break

        elif chackWin(item.xcor(), item.pencolor(), the_winning_turtle) == False:
            print(f"the winner is: {item.pencolor()}. you are loser!!!\n\ngame over!!! ")
            game = False
            break


screen.exitonclick()



