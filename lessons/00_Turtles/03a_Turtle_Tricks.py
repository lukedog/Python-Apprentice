"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

tina.forward(120)
tina.pencolor("pink")
tina.left(100)
tina.pencolor("pink")

tina.forward(120)
tina.pencolor("cyan")
tina.left(100)
tina.pencolor("cyan")


tina.left(30)
tina.forward(160)



turtle.exitonclick()                    # Close the window when we click on it
