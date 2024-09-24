""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle                          
turtle.setup(width=600, height=600)     

tina = turtle.Turtle()  
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screentina.penup()
tina.pendown()
#set_turtle_image(tina,"pikachu.gif")
tina.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
tina.color("cyan")
tina.begin_fill()

for i in range(5):
    tina.forward(50)
    tina.left(72)

tina.goto(60,140) 
tina.end_fill()



turtle.exitonclick() 

... # Your Code Here