import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image = [rock, paper, scissors]
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("Users Choice")
print(game_image[users_choice])

comp_choice = random.randint(0, 2)

print("Computers Choice")
print(game_image[comp_choice])

if users_choice >= 3 or users_choice < 0:
    print("You typed an invalid number, You Lose.  ☠")
elif users_choice == 0 and comp_choice == 2:
    print("You win! 🎉")
elif comp_choice == 0 and users_choice == 2:
    print("You lose.  ☠")
elif comp_choice > users_choice:
    print("You lose. ☠")
elif users_choice > comp_choice:
    print("You win!🎉 ")
elif comp_choice == users_choice:
    print("It's a draw.")
