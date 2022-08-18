from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
               "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", "/"]

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(1, nr_letters + 1):
    #     password.append(random.choice(letters))

    # for num in range(1, nr_numbers + 1):
    #     password.append(random.choice(numbers))
    #
    # for sym in range(1, nr_symbols + 1):
    #     password.append(random.choice(symbols))

    password_list = password_letter + password_sym + password_num

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# new_password = ""
# for char in password_list:
#     new_password += str(char)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email},"
                                                              f" \nPassword: {password}\n Is it ok to Save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                # username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
# create_image(width, height, image=)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# input boxes
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "vishpetkar18@gmail.com")

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
