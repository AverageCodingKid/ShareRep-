import tkinter
from tkinter import *
from tkinter import font
import pyperclip

root = Tk()
root.geometry("300x300")  # Set window size
root.title("Text Editor 📃")  # Set window title
root.resizable(False, False)  # Disable resizing

def saved():
    pyperclip.copy(text.get("1.0", END))
    
    if color_var.get() == "Black":
        print("Test Success")
        text.config(foreground="Black")
    elif color_var.get() == "Red":
        print("Test Success")
        text.config(foreground="Red")
    elif color_var.get() == "Blue":
        print("Test Success")
        text.config(foreground="Blue")

    if font_var.get() == "Comic Sans MS":
        text.config(font=("Comic Sans MS", 12)) # replace "Comic Sans MS
    elif font_var.get() == "Verdana":
        text.config(font=("Verdana", 12))
    elif font_var.get() == "Arial":
        text.config(font=("Arial", 12))

    print("Exit Code 0")


    
    
text = Text(root)
text.place(width=300, height=250, y=30)

font_var = StringVar(root)
font_var.set("Font 🔤")
font = OptionMenu(root, font_var, "Arial", "Comic Sans MS", "Verdana")
font.place(x=0, width=150)

color_var = StringVar(root)
color_var.set("Text Color 🌈")
color = OptionMenu(root, color_var, "Black", "Red", "Blue")
color.place(x=150, width=150)


changes = Button(root, text="Save Changes ✔", command=saved)
changes.place(y=275, width=300)

root.mainloop()