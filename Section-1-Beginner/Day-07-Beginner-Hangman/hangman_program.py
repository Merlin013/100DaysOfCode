import random
import hangman_words
import hangman_art


#word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
display = []

print(hangman_art.logo)

for _ in range(word_length):
    display += '_'


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already guessed {}".format(guess))

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print("The word was: {}".format(chosen_word))

    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])