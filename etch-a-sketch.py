from turtle import Turtle,Screen

screen=Screen()
tim=Turtle()


def forward():
    tim.fd(20)

def right():
    tim.right(10)

def left():
    tim.left(10)

def back():
    tim.back(20)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen.listen()
screen.onkey(forward,"w")
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(back,"s")

screen.onkey(clear,"c")


screen.exitonclick()