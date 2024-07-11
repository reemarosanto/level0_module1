from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# Write a Python program that asks the user for two numbers.
    number_1 = simpledialog.askstring(title='Greeter', prompt="Enter a number")
    number_2 = simpledialog.askstring(title='Greeter', prompt="Enter a second number")
    number_3 = int(number_1) + int(number_2)
    number_4 = int(number_1) - int(number_2)
    number_5 = int(number_1) * int(number_2)
    number_6 = int(number_1) / int(number_2)
# Then ask the user if the would like to add, subtract, multiply, or divide.
    operation = simpledialog.askstring(title='Greeter', prompt="Would you like to add, subtract, multiply, or divide?")
#Use if-else statements to provide the desired math operation on the number and display the result.
    if operation == "add":
        messagebox.showinfo(message="Your equation is equal to " + str(number_3))
    if operation == "subtract":
        messagebox.showinfo(message="Your equation is equal to " + str(number_4))
    if operation == "multiply":
        messagebox.showinfo(message="Your equation is equal to " + str(number_5))
    if operation == "divide":
        messagebox.showinfo(message="Your equation is equal to " + str(number_6))