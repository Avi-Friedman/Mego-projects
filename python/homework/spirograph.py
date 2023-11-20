import random
from turtle import Turtle, Screen
#function for ellipse.
def ellipse():
    spirograph.circle(400, 50)
    spirograph.circle(27, 130)


spirograph = Turtle()
spirograph.speed(20)
# start from a lower place
spirograph.penup()
spirograph.left(270)
spirograph.forward(20)
spirograph.pendown()

for i in range (70):
    spirograph.color(random.random(),random.random(),random.random())
    ellipse()
    ellipse()
    spirograph.left(6)
    spirograph.penup()
    spirograph.forward(15)
    spirograph.pendown()

my_screen = Screen()
my_screen.exitonclick()