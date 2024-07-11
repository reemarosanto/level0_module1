import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    my_turtle.color('red')
    my_turtle.pencolor('red')
    my_turtle.hideturtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='Greeter', prompt="What shape do you want to draw: triangle, square or circle?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        my_turtle.goto(-55, 0)
        my_turtle.goto(0, 55)
        my_turtle.goto(55, 0)
        my_turtle.goto(0, 0)
        turtle.done()
    if shape == "square":
        my_turtle.color('blue')
        my_turtle.pencolor('blue')
        my_turtle.goto(-75, 0)
        my_turtle.goto(-75, 75)
        my_turtle.goto(0, 75)
        my_turtle.goto(0, 0)
        turtle.done()
    if shape == "circle":
        my_turtle.pencolor('purple')
        my_turtle.circle(radius=50, steps=30)
        turtle.done()
    # Call the turtle .done() method
