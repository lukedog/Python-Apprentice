
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = ... # Calculate angle from number of sides
    
    for i in range(...):                 # Loop through the number of sides
        ...                              # Move tina forward by the forward distance
        ...                              # Turn tina left by the left turn
for i in range(4):
    tina.forward(50)                        # Draw a square
    tina.left(90)

tina.penup()   
tina.left(90)                         # Move tina to another spot on the screen
tina.forward(70)

tina.pendown()

for i in range(5):
    tina.forward(50)
    tina.left(72)

tina.penup()

tina.forward(70)
    
tina.left(90)                       
tina.forward(120) 

tina.pendown()
for i in range(6):
    tina.forward(50)
    tina.left(60) 
                                      # Move tina to another spot on the screen

draw_polygon(...)                        # Draw a hexagon


turtle.exitonclick()                     # Close the window when we click on it
