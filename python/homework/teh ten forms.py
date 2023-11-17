from turtle import Turtle, Screen
import random
painter = Turtle()
degrees = 3
for i in range(10):
    for i in range(degrees):
        painter.right(360/degrees)
        painter.forward(80)
    degrees += 1
    painter.color(random.random(), random.random(), random.random())

my_screen = Screen()
my_screen.exitonclick()




