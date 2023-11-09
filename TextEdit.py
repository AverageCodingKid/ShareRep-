import tkinter
from tkinter import *
from tkinter import font
import pyperclip


root = Tk()
root.geometry("300x300")  # Set window size
root.title("Text Editor 📃")  # Set window title
root.resizable(False, False)  # Disable resizing

def saved():
    text_content = text.get("1.0", END)
    pyperclip.copy(text_content)  # Copy text to clipboard

    selected_font = font_var.get()
    if selected_font == "Comic Sans MS":
        text.config(font=("Comic Sans MS", 12))
    elif selected_font == "Verdana":
        text.config(font=("Verdana", 12))
    elif selected_font == "Arial":
        text.config(font=("Arial", 12))

    selected_color = color_var.get()
    if selected_color == "Black":
        text.config(foreground="Black")
    elif selected_color == "Red":
        text.config(foreground="Red")
    elif selected_color == "Blue":
        text.config(foreground="Blue")

    state = Label(root, text="Copied to Clipboard 📋")
    state.place(x=90, y=140)
    state.after(3000, state.destroy)
    root.update()


text = Text(root)
text.place(width=300, height=250, y=30)

font_var = StringVar(root)
font_var.set("Arial")
font = OptionMenu(root, font_var, "Arial", "Comic Sans MS", "Verdana")
font.place(x=0, width=150)

color_var = StringVar(root)
color_var.set("Black")
color = OptionMenu(root, color_var, "Black", "Red", "Blue")
color.place(x=150, width=150)

changes = Button(root, text="Save Changes ✔", command=saved)
changes.place(y=275, width=300)

root.mainloop()