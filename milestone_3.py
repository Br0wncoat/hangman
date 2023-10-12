import random

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word!")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('Please enter a single letter: ')
        if len(guess) != 1 or guess.isalpha() is False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            check_guess(guess)


word_list = ['Apple', 'Grapes','Pineapple','Mango', 'Orange']
word = random.choice(word_list).lower()
ask_for_input()

