import tkinter

# Creating a window
window = tkinter.Tk()

# Change the title of the window
window.title("GUI Practice program")

# To specify the default size of the window in pixels
window.minsize(width=500, height=300)

# to add padding around components
window.config(padx=20, pady=20)

# Labels
# Crating a label, but it will not show on screen by default
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24))

# we can also change values of keywords by assigning new values like dictionaries, or by using config()
my_label["text"] = "New Text1"
my_label.config(text="new text 2")


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Creating a button, has a property called command to run functions when pressed
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry for taking inputs in the window
input = tkinter.Entry(width=15)
input.pack()

# To get the string that was input by the user
input.get()



# By using the pack() method the label can be seen on the screen, in the center of the screen
my_label.pack()

# To keep the window open on screen; Has to be at the very end of the program
window.mainloop()
