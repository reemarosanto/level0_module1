from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number_1 = simpledialog.askstring(title='Greeter', prompt="Enter a number")
    number_2 = simpledialog.askstring(title='Greeter', prompt="Enter a second number")
    number_3 = int(number_2) + int(number_1)
    messagebox.showinfo(message="The sum of the numbers you entered is " + str(number_3))


# Write a Python program that asks the user for two numbers.

# Display the sum of the two numbers to the user
