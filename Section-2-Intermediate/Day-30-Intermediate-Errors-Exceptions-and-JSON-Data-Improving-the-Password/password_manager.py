from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            # username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No datafile Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
website_input = Entry(width=22)
website_input.grid(row=1, column=1)
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

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
