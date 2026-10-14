# from tkinter import *
# window = Tk()
# window.title("Event Handler")
# window.geometry("100x100")
# def handle_keypress (event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
# window.bind("<Key>", handle_keypress)
# def handle_click(event):
#     print("\nThe button was clicked!")
# button = Button (text="Click me!")
# button.pack()
# button.bind("<Button-1>", handle_click)
# window.mainloop()

from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")
button = Button (root, text="Scan for Virus", command=msg)
button.place (x = 40, y = 80)
root.mainloop()