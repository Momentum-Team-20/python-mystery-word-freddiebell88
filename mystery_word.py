import random


# def get_letter_guess():


def replace_letter(str):
    for character in str:
        if character in str:
            str = str.replace('_', character)


def play_game(file):
    with open(file) as reader:
        text = reader.read()
        word_list = text.split()
        # print(word_list)
        answer = random.choice(word_list)
        print(answer)
        letters = [letter for letter in answer]
        print(letters)
        blank_letters = [letter.replace(letter, '_') for letter in letters]
        print(blank_letters)
        game_board = "".join(blank_letters)
        print(game_board)
        guess = input("Guess a letter: ")
        print(guess)
        replace_letter()
        

        # if guess in letters:
        #     print(letter)
        # else:
        #     print('_')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Guess the word.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
