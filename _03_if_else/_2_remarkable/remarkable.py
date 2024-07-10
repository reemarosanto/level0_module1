import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    user_name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    if str(user_name) == "SpongeBob":
        messagebox.showinfo(message="You live in a pineapple!")
    if str(user_name) == "Patrick":
        messagebox.showinfo(message="You live in Bikini Bottom!")
    if str(user_name) == "Sandy":
        messagebox.showinfo(message="You are a squirrel!")
    if str(user_name) == "Squidward":
        messagebox.showinfo(message="You are a squid!")