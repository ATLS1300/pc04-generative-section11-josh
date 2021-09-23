"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: YOUR NAME HERE

********* HEY, READ THIS FIRST **********

This code is a type of generative art. It will make a large spirograph with 2 funky spirals in the middle.
First, it will create a completely randomized spirograph. The colors the turtle use will be randomized.
Second, it will create 2 funky spirals at the same time!
The colors and scale of those funky spirals will also be randomized.

"""
import turtle
import math, random

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
panel.bgcolor(0,0,0)
turtle.speed(10)
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h)


# Defined the color palette I will be using as well as all the varibales throughout the code.
# Defined a random variable that I will call upon later in the code. IT randomizes the scale of the funky spirals

colorPalette = [("lightcyan"), ("#D5FFF3"), ("#AF9AB2"), ("#820B8A"), ("#672A4E")]
ANGLES = range(0,1080)
a = 24
b = 25
scale = random.randint(5,15) #Created a variable that stores the random integer for the scale

#Defined the three turtles I will be using for the code.

spirograph = turtle.Turtle()
funkySpiral1 = turtle.Turtle()
funkySpiral2 = turtle.Turtle()
funkySpiral3 = turtle.Turtle()
funkySpiral4 = turtle.Turtle()

turtle.tracer(0)
turtle.hideturtle()

size = 25
sides = 4 
angle = 180/sides

inc = 2
numIt = int(360/inc)
innerCirc = 600

# Borrowed code from Grace Park. She is in Section 011 with me
# It creates a spirograph. The color of the spirograph is completely randomized

spirograph.up()
spirograph.goto(275,50)

for iteration2 in range(numIt):
    spirograph.down()
    spirograph.color(random.choice(colorPalette)) # Radnomizes the color
    for iteration1 in range (sides):
        spirograph.forward(size)
        spirograph.right(angle)
    spirograph.up()
    spirograph.forward(innerCirc)
    spirograph.right(inc)
    
spirograph.up()
spirograph.hideturtle()

# This for loop creates 2 funky spirals simultaneously
# Both of them are randomized in their scales and colors

funkySpiral1.up()
funkySpiral1.goto(-150,-150)
funkySpiral2.up()
funkySpiral2.goto(150,-150)

for angle in ANGLES:
    angle = math.radians(angle) # overwrites input to radians (required!)
    funkySpiral1.color(random.choice(colorPalette)) # Randomizes the color
    funkySpiral2.color(random.choice(colorPalette))
    funkySpiral1.down()
    funkySpiral2.down()
    X = (angle - 1.6*math.cos(a*angle))
    Y = (angle - 1.6*math.cos(b*angle))
    A = -1*((angle - 1.6*math.cos(a*angle)))
    B = (angle - 1.6*math.cos(b*angle))
    X*=scale # make the image larger so it's visible
    Y*=scale
    A*=scale
    B*=scale
    funkySpiral1.goto((X)-150,(Y)-150)
    funkySpiral2.goto((A)+150,(B)-150)
    
funkySpiral1.up()
funkySpiral2.up()
funkySpiral1.hideturtle()
funkySpiral2.hideturtle()

# This for loop creates 2 funky spirals simultaneously
# Both of them are randomized in their scales and colors

funkySpiral3.up()
funkySpiral3.goto(-150,0)
funkySpiral4.up()
funkySpiral4.goto(150,0)

for angle in ANGLES:
    angle = math.radians(angle) # overwrites input to radians (required!)
    funkySpiral3.color(random.choice(colorPalette)) # Randomizes the color
    funkySpiral4.color(random.choice(colorPalette))
    funkySpiral3.down()
    funkySpiral4.down()
    C = (angle - 1.6*math.cos(a*angle))
    D = (angle - 1.6*math.cos(b*angle))
    E = -1*((angle - 1.6*math.cos(a*angle)))
    F = (angle - 1.6*math.cos(b*angle))
    C*=scale # make the image larger so it's visible
    D*=scale
    E*=scale
    F*=scale
    funkySpiral3.goto((C)-150,(D))
    funkySpiral4.goto((E)+150,(F))

funkySpiral3.up()
funkySpiral4.up()
funkySpiral3.hideturtle()
funkySpiral4.hideturtle()

panel.update()
turtle.done()

