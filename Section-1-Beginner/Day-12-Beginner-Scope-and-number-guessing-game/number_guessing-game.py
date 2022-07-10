import random

print("Welcome to the Number Guessing game!!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
guessed_correct = False
number = random.randint(1, 100)
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

while not guessed_correct:

    print("You have {} attempts remaining to guess the number.".format(guesses))
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You have guessed correctly!!")
        exit(0)
    elif guess < number:
        print("Your guess is a little low, guess again.")
        guesses -= 1
    elif guess > number:
        print("Your guess is a little high, guess again.")
        guesses -= 1

    if guesses == 0:
        print("You have {} attempts remaining to guess the number.".format(guesses))
        print("You have lost!")
        guessed_correct = True
