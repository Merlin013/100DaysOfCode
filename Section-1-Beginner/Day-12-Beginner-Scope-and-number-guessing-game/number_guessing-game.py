import random


def game_mode():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        guesses = 10
        return guesses
    else:
        guesses = 5
        return guesses


print("Welcome to the Number Guessing game!!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
guessed_correct = False
guess_num = game_mode()

while not guessed_correct:

    print("You have {} attempts remaining to guess the number.".format(guess_num))
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You have guessed correctly!!")
        exit(0)
    elif guess < number:
        print("Your guess is a little low, guess again.")
        guess_num -= 1
    elif guess > number:
        print("Your guess is a little high, guess again.")
        guess_num -= 1

    if guess_num == 0:
        print("You have {} attempts remaining to guess the number.".format(guess_num))
        print("You have lost!")
        guessed_correct = True
