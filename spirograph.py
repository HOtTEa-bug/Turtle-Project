import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    col = (r, b, g) #tuple
    return col


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100) #radius=100
        #current_heading = tim.heading()
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()