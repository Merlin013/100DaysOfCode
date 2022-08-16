from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(input.get())
    km_ans = miles * 1.609344
    ans_label.config(text=f"{km_ans:.2f}")


input = Entry(width=20)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

is_equal_to = Label(text="is equal to ")
is_equal_to.grid(row=1, column=0)

ans_label = Label(text="0")
ans_label.grid(row=1, column=1)

button = Button(text="Convert", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
