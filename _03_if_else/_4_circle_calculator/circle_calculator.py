# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius = simpledialog.askstring(title='Greeter', prompt="Enter the radius of your circle")
    user_input = simpledialog.askstring(title='Greeter', prompt="Would you like to calculate the area or circumference of your circle?")
    if user_input == "area":
        area = math.pi * int(radius) * int(radius)
        messagebox.showinfo(message="The area of your circle is " + str(area))
    if user_input == "circumference":
        circumference = math.pi * int(radius) * 2
        messagebox.showinfo(message="The circumference of your circle is " + str(circumference))
#Area = πr^2
#Circumference = 2πr 