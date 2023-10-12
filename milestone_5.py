import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word and guess not in self.list_of_guesses:
            print(f"Good guess! {guess} is in the word!")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters = self.num_letters-1
            print(self.num_letters)

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            guess = input('Please enter a single letter: ')
            if len(guess) != 1 or guess.isalpha() is False:
                print(
                    "Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            if self.num_letters == 0 or self.num_lives == 0:
                break

    def play_game(self):
        self.num_lives = 5
        while True:
            if self.num_lives == 0:
                print("You lost")
                break
            if self.num_letters == 0:
                print("Congratulations! You have won the game!")
                break
            self.ask_for_input()

word_list=['Apple', 'Grapes', 'Pineapple', 'Mango', 'Orange']
game = Hangman(word_list)
game.play_game()
