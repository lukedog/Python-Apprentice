"""
Use boolean variables to control program logic between two different code
paths.
"""



# TODO)
#  1. Use a boolean variable to indicate if it is the weekend.
#     Display a different message to the user depending on whether it is
#     the weekend or not.
#  2. Use a boolean variable to indicate if a student passed an exam.
#     Display a different message to the user depending on whether they
#     passed or not.
#  3. Use a boolean variable to indicate if a game is over. When the game
#     is over, tell the user.
#  4. Use two boolean variables, one to indicate if a shape should be red,
#     the other to indicate if the shape is to be square. When both
#     variables are true, use a turtle to draw a red square.
pass
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