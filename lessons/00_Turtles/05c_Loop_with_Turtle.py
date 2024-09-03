
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

import turtle                          
turtle.setup (width=600, height=600)   

tina = turtle.Turtle() 

tina.forward(120) 
tina.right(72) 
tina.pencolor("blue")

for i in range(4):
    tina.forward(120)   # type: ignore
    tina.right(72)  # type: ignore



... # Your code here
