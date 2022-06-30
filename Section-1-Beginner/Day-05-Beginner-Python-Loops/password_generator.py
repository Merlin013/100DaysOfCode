# Password generator project

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", "/"]

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters do you want in your password? \n"))
nr_numbers = int(input("How many numbers do you want?\n"))
nr_symbols = int(input("How many Symbols do you want?\n"))

password = []

for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for num in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

for sym in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
new_password = ""

for char in password:
    new_password += str(char)
print(new_password)
