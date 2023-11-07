import random
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
file = 'words.txt'


def validate_guess(guess_copy, guessed_letters):
    guess_is_valid = False
    while not guess_is_valid:
        if len(guess_copy) != 1 or not guess_copy.isalpha():
            guess_copy = input(Fore.YELLOW + 'Invalid guess. Try again: ')
        elif guess_copy in guessed_letters:
            guess_copy = input(Fore.YELLOW + f'You have already guessed {guess_copy}.'
                               ' Try again: ')
        else:
            guess_is_valid = True
    return guess_copy.lower()


def replace_letter(str):
    for character in str:
        if character in str:
            str = str.replace('_', character)


def build_game_board(answer, guessed_letters):
    correct_letters = []
    for letter in answer:
        if letter in guessed_letters:
            correct_letters.append(letter)
        else:
            correct_letters.append("_")
    print(" ".join(correct_letters))


def play_game(file):
    with open(file) as reader:
        text = reader.read()
        word_list = text.split()
        answer = random.choice(word_list)
        letters = [letter for letter in answer]
        game_board = [letter.replace(letter, '_') for letter in letters]
        print(f'Your word has {len(answer)} letters.')
        guessed_letters = []
        guess_limit = 8
        wrong_guesses = 0
        while wrong_guesses < guess_limit:
            guess = input("Guess a letter: ").lower()
            guess = validate_guess(guess, guessed_letters)
            guessed_letters.append(guess)
            if guess in answer:
                print(Back.GREEN + "correct!")
                for index in range(len(answer)):
                    if guess == answer[index]:
                        game_board[index] = guess
                build_game_board(answer, guessed_letters)
            else:
                print(Back.RED + "incorrect!")
                wrong_guesses += 1
                print(f'You have used {wrong_guesses} of 8 guesses.')
                if wrong_guesses == guess_limit:
                    print(f'You ran out of guesses. The word was {answer}.')    
            if "_" not in game_board:
                print(Back.YELLOW + Fore.MAGENTA + "VICTORY!")
                break
    play_again = input("Do you want to play again? y/n: ").lower()
    if play_again == 'y':
        play_game(file)
    elif play_again == 'n':
        exit()
    else:
        print("Invalid input.")


if __name__ == "__main__":
    play_game(file)
