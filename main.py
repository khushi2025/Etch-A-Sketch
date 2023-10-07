from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
def move_forward():

    timmy.forward(10)
def move_backward():

    timmy.backward(10)

def move_clockwise():
    # timmy.tilt(345)
    timmy.setheading(timmy.heading()+345)

def move_anticlockwise():
    # timmy.tilt(15)
    timmy.setheading(timmy.heading() + 15)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.setposition(0,0)
    timmy.setheading(0)
    timmy.pendown()
    

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="c",fun=clear)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="a",fun=move_anticlockwise)




screen.exitonclick()