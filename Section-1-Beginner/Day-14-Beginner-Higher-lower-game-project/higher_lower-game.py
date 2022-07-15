from art import logo, vs
from game_data import data
import random
import os


def format_data(account):
    """Formats account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return "{}, a {}, from {}".format(account_name, account_desc, account_country)


def check_answer(guess, a_followers, b_followers):
    """To check if user is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print("Compare A: {}".format(format_data(account_a)))
    print(vs)
    print("Against B: {}".format(format_data(account_b)))

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("cls")
    print(logo)

    if is_correct:
        score += 1
        print("You're right! Current score {}".format(score))
    else:
        game_should_continue = False
        print("Sorry you are wrong! Final score {}".format(score))
