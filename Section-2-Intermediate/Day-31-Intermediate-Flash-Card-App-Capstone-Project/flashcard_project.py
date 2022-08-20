from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    # data = pandas.read_csv("./data/german_words.csv", encoding='latin1')
    data = pandas.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv("./data/german_words.csv", encoding='latin1')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Tkinter method 'after' must be used if we need to create a delay in the app. We cannot use time.sleep inside of the
# tkinter mainloop. Check out http://tcl.tk/man/tcl8.6/TclCmd/after.htm for more info
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text=f"Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"Word", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_img, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
check_button = Button(image=right_img, command=is_known)
check_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
