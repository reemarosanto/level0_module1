from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo(message="I have been alive for 11 years...these are all of the ages I have been alive for...")
    for i in range(12):
        print(i)
