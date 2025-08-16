from turtle import Turtle , Screen, xcor
import random
screen = Screen()

is_race_on = False
screen.setup(width= 600, height= 500)
user_bet = screen.textinput("make your bet", "which turtle gonna won pick a color: ")
colors = ["green","blue","red","pink","brown","yellow"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6) :
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup ()
    new_turtle.goto(x= -290,y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor() > 270:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet :
                print (f"you won! {winning_turtle} turtle is the winning turtle.")
            else :
                print (f"you lost! {winning_turtle} turtle is the winning turtle.")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()

