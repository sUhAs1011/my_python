from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)

is_race_on=False
colours=["red","blue","yellow","green","orange","pink"]
user_bet=screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Choose color: ")
all_turtles=[]


x=-230
y=[-70,-40,-10,20,50,80]


for i in range(len(colours)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.goto(x,y[i])
    new_turtle.color(colours[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor()>230:
                is_race_on=False
                winning_color=turtle.pencolor()
                if winning_color==user_bet:
                    print(f"Congratulations!!! {turtle.pencolor()} has won the race")
                    
                else:
                     print(f"{turtle.pencolor()} has won the race, You Loose")
        
            rand_distance=random.randint(1,10)
            turtle.forward(rand_distance)




screen.exitonclick()