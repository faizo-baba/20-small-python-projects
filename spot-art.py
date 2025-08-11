import turtle as turtle_module 
import random
from turtle import Screen

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fast")
tim.penup ()
tim.hideturtle()



colors_list = [(201, 165, 111), (235, 239, 245), (145, 75, 51), (221, 202, 138), (57, 92, 123), (167, 151, 47), (131, 34, 24), (135, 163, 183), (49, 117, 88), (197, 92, 73), (67, 47, 41), (16, 97, 75), (148, 179, 149), (118, 74, 77), (167, 143, 154), (234, 176, 166), (144, 23, 28), (59, 41, 44), (36, 59, 70), (186, 86, 92), (183, 204, 176), (40, 76, 80), (89, 145, 125), (47, 64, 84), (222, 174, 178), (28, 67, 60), (177, 197, 204)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1,number_of_dots + 1) :
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0 :
        tim.setheading (90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)   


screen = Screen ()
screen.exitonclick()
