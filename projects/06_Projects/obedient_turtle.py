"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error


# TODO)
#   1. Create a turtle.
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass

none = simpledialog.askfloat("What shape would you like? A square, a triangle, or a circle? ")


import turtle                          
turtle.setup(width=600, height=600)     

tina = turtle.Turtle() 


for i in range(4): 
    tina.forward(50)
    tina.left(90)
     
tina.penup()
tina.forward(90)
tina.pendown()


