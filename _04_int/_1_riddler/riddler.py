from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
 #Write a python program that asks the user a minimum of 3 riddles.
    riddle_1 = simpledialog.askstring(title='Greeter', prompt="What weighs more, a pound of feathers or a pound of stones?")
    riddle_2 = simpledialog.askstring(title='Greeter', prompt="David's father has three sons: Snap, Crackle, and _____?")
    riddle_3 = simpledialog.askstring(title='Greeter', prompt="What is more useful when it is broken?")
    riddle_4 = simpledialog.askstring(title='Greeter', prompt="What's 3/7 chicken, 2/3 cat, and 2/4 goat?")
    riddle_5 = simpledialog.askstring(title='Greeter', prompt="What 4-letter word can be written forward, backward or upside down, and can still be read from left to right?")
# You can look at riddles.com if you don't already know any riddles.
# Collect the response of each riddle from the user and compare their
 # answers to the correct answer.
    if riddle_1 == "They both weigh a pound":
        score = score + 1
    else: score = score - 1
    if riddle_2 == "David":
        score = score + 1
    else: score = score - 1
    if riddle_3 == "An egg":
        score = score + 1
    else: score = score - 1
    if riddle_4 == "Chicago":
        score = score + 1
    else: score = score - 1
    if riddle_5 == "NOON":
        score = score + 1
    else: score = score - 1

# Use a variable to keep track of the correctly answered riddles

# After all the riddles have been asked, tell the user how many they got
#  correct
    messagebox.showinfo(message="Your score is " + str(score))