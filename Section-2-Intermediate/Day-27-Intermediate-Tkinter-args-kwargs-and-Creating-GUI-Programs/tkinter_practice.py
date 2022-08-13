import tkinter

# Creating a window
window = tkinter.Tk()

# Change the title of the window
window.title("GUI Practice program")

# To specify the default size of the window in pixels
window.minsize(width=500, height=300)

# Labels
# Crating a label, but it will not show on screen by default
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24))

# By using the pack() method the label can be seen on the screen, in the center of the screen
my_label.pack()



# To keep the window open on screen; Has to be at the very end of the program
window.mainloop()
