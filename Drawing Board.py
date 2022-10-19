from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(30)
def move_back():
    tim.backward(30)
def move_cc():
    new_h= tim.heading()+10
    tim.setheading(new_h)
def move_c():
    new_h = tim.heading() - 10
    tim.setheading(new_h)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "s", fun= move_back)
screen.onkey(key= "a", fun= move_cc)
screen.onkey(key= "d", fun= move_c)
screen.onkey(key= "c", fun= clear)

screen.exitonclick()

