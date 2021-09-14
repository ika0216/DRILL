import turtle
import random

def drunken_move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_down():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_move_up, 'w')
turtle.onkey(drunken_move_down, 's')
turtle.onkey(drunken_move_left, 'a')
turtle.onkey(drunken_move_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
