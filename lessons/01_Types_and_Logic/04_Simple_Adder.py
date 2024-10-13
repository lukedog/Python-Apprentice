"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog, Tk 


window = Tk()  

window.withdraw()  

num1 = simpledialog.askfloat(None,"What is your number?" )


num2 = simpledialog.askfloat(None,"What is your number?" )

messagebox.showinfo(message=num1+num2)
# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method4

# Ask the user for the first number   

# Ask the user for the second number

# Display the sum of the two numbers 

# Keep the window open

