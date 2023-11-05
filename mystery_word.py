import random
file = 'words.txt'


def validate_guess(guess, guessed_letters):
    if len(guess) != 1:
        guess = input('Invalid guess. Try again: ')
        return guess.lower()
    elif guessed_letters:
        if guess in guessed_letters:
            guess = input(f'You have already guessed {guess}. Try again: ')
            # after this line it is saying any guess is incorrect
            return guess.lower()

    # else:
    #     return True
# def validate_guess():
#     guess = input("Guess a letter: ").lower()
#     guessed_letters = []
#     if len(guess) == 1:
#         return guess
#     elif guess not in guessed_letters:
#         guessed_letters.append(guess)
#         return guess
#     elif guess in guessed_letters:
#         guess_again = input("Already guess. Guess again: ")
#         return guess_again
#     else:
#         invalid_guess = input("Invalid guess. Please guess again: ")
#         return invalid_guess
    # while len(guess) != 1:
    #     guess = input('Invalid guess. Try again: ')

    # while guessed_letters:
    #     if guess in guessed_letters:
    #         guess = input(f'You have already guessed {guess}. Guess again: ')

    # return guess.lower()


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
        print(answer)
        letters = [letter for letter in answer]
        game_board = [letter.replace(letter, '_') for letter in letters]
        print(f'Your word has {len(answer)} letters.')
        print(game_board)
        guessed_letters = []
        guess_limit = 8
        wrong_guesses = 0
        while wrong_guesses < guess_limit:
            guess = input("Guess a letter: ").lower()
            validate_guess(guess, guessed_letters)
            guessed_letters.append(guess)
            print(guessed_letters)
            if guess in answer:
                print("correct!")
                for index in range(len(answer)):
                    if guess == answer[index]:
                        game_board[index] = guess
                        # print(game_board)
                        build_game_board(answer, guessed_letters)
            else:
                print("incorrect!")
                wrong_guesses += 1
                print(f'You have used {wrong_guesses} of 8 guesses.')
                if wrong_guesses == guess_limit:
                    print(f'You ran out of guesses. The word was {answer}.')    
            if "_" not in game_board:
                print("VICTORY!")
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
    # import argparse
    # from pathlib import Path
    # parser = argparse.ArgumentParser(
    #     description='Guess the word.')
    # parser.add_argument('file', help='file to read')
    # args = parser.parse_args()

    # file = Path(args.file)
    # if file.is_file():
    #     play_game(file)
    # else:
    #     print(f"{file} does not exist!")
    #     exit(1)
