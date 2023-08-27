import turtle as t
import random
t.colormode(255)
tim = t.Turtle()


########### Challenge 3 - Draw Shapes ########

def random_choice():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  random_color=(r,g,b)
  return random_color

directions=[0,90,180,270]

def movement(directions):
    for _ in range(100):
      tim.pensize(10)
      tim.fd(30)
      tim.setheading(random.choice(directions))
      tim.color(random_choice())


movement(directions)