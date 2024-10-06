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
"""
Boolean Variable Demo
"""

# Boolean is a variable type that has two values:
#   True
#   False
# Just like int, double, and string variables, boolean variables can be
# created by writing the variable name followed by = True or = False
#   boolean_var = True
#   boolean_var = False
#
# Boolean variables or values can be used directly in if and elif statements:
#   boolean_var = True
#   if boolean_var:
#       print('boolean_var was True!')
#
# Notice that if boolean_var == True: isn't necessary.
#
# Boolean values are created when doing inequality comparisons (<, > ==)
# between variables or values
#   boolean_var = 5 == 5            # True
#   is_Keith = name == 'Keith'      # True
#   is_weekday = day == 'Saturday'  # False
#
# Boolean variables can be toggled, i.e. switched, using the 'not' keyword
#   boolean_var = True
#   boolean_var2 = not boolean_var  # False

# Two boolean variables
boolean_var1 = True
boolean_var2 = False

# NOTE - boolean_var1 == True is not necessary
if boolean_var1:
    print('boolean_var1 is True!')
    if boolean_var2:
        print('boolean_var2 is True!')
    else:
        print('boolean_var2 is False!')
else:
    print('boolean_var1 is False!')

boolean_var3 = True
for i in range(4):
    print('boolean_var3 is: ' + str(boolean_var3))
    boolean_var3 = not boolean_var3

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

    # Set up the screentina.penup()
tina.pendown()
#set_turtle_image(tina,"pikachu.gif")
tina.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
tina.color("red")
tina.begin_fill()

for i in range(4):
    tina.forward(90)
    tina.left(90)

tina.goto(60,140) 
tina.end_fill()



turtle.exitonclick() 