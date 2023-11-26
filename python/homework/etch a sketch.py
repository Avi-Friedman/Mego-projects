from turtle import Turtle, Screen


def forward():
    etch.forward(10)
def beck():
    etch.backward(10)
def left():
    etch.left(10)
def right():
    etch.right(10)

def clear():
    etch.penup()
    etch.home()
    etch.clear()
    etch.pendown()


etch = Turtle()
screen_etch = Screen()
screen_etch.setup(width=500, height=400)
screen_etch.listen()

screen_etch.onkey(key = "w", fun = forward)
screen_etch.onkey(key = "s", fun = beck)
screen_etch.onkey(key = "a", fun = left)
screen_etch.onkey(key = "d", fun = right)
screen_etch.onkey(key = "c", fun = clear)

screen_etch.exitonclick()



