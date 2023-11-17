from turtle import Turtle, Screen
import random
prater = Turtle()
prater.pensize(12)
prater.shape("turtle")
turn = [90, 180, 270, 360]
for i in range (60):
    prater.color(random.random(), random.random(), random.random())
    num_random = random.randint(1, 35)
    random_turn = random.choice(turn)
    prater.forward(num_random)
    prater.left(random_turn)
    prater.forward(num_random)

my_screen = Screen()
my_screen.exitonclick()




