import turtle
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    date = "07/10"
    user_birthday = simpledialog.askstring(title='Greeter', prompt="Enter your birthday (mm/dd)")
    if user_birthday == date:
        messagebox.showinfo(message="Happy birthday!")
    messagebox.showinfo(message="Have a merry unbirthday!")

