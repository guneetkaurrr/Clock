# Program that gives the current time on a respresentation of a clock.

import datetime
import turtle

# Turtle 1, the clock shape itself
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(2)
alex.color("black")
alex.shape("square")
alex.up()
alex.speed(0)

for i in range(12):
    alex.forward(150)
    alex.stamp()
    alex.backward(150)
    alex.right(360/12)

# Variables
hour = datetime.datetime.now().hour % 12
minute = datetime.datetime.now().minute

# Turtle 2, the hour hand
hour_hand = turtle.Turtle()
hour_hand.color("black")
hour_hand_angle = (hour + (minute / 60)) * 30 - 90
hour_hand.right(hour_hand_angle)
hour_hand.forward(100)
hour_hand.hideturtle()

# Turtle 3, the minute hand
minute_hand = turtle.Turtle()
minute_hand.color("black")
minute_hand.left(90)
minute_hand.right(minute * 6)
minute_hand.forward(120)
minute_hand.hideturtle()

wn.exitonclick()
