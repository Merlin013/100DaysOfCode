from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
window.minsize(width=300, height=100)


def button_pressed():
    num = float(input.get())
    converted_value = num * 1.609344
    ans_label.config(text=f"{converted_value:.2f}")


input = Entry(width=20)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

calculate_label = Label(text="is equal to ")
calculate_label.grid(row=1, column=0)

ans_label = Label(text="0")
ans_label.grid(row=1, column=1)

button = Button(text="Convert", command=button_pressed)
button.grid(row=2, column=1)

window.mainloop()
