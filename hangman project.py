# MAIN PROJECT, first project!
    from functions import (opening, choose_word, check_win, show_hidden_word, check_valid_input, try_update_letter_guessed)

def main():
    old_letters_guessed = []
    num_of_tries = 1
    HANGMAN_PHOTOS = {1: '''
    x-------x
    ''',
                      2: '''
         x-------x
    |
    |
    |
    |
    |
''', 3: '''    x-------x
    |       |
    |       0
    |
    |
    |''', 4: '''
        x-------x
    |       |
    |       0
    |       |
    |
    |''', 5: '''
        x-------x
    |       |
    |       0
    |      /|\
    |
    |''', 6: '''
       x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
''', 7: '''
     x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |'''}

    print(opening)
    # ask user for file path and an index
    file_path = input("insert file path: ")
    index = int(input("Insert an index: "))
    secret_word = choose_word(file_path, index)  # chooses a word

    print(HANGMAN_PHOTOS[num_of_tries])

    # work
    while num_of_tries < 6 and (check_win(secret_word, old_letters_guessed) == False):
        show_hidden_word(secret_word, old_letters_guessed)
        letter_guessed = input("Insert a letter: ")
        if check_valid_input(letter_guessed, old_letters_guessed):
            old_letters_guessed = try_update_letter_guessed(letter_guessed, old_letters_guessed)
            if letter_guessed not in secret_word:
                num_of_tries += 1
                print("):")
                print(HANGMAN_PHOTOS[num_of_tries])
        else:
            print("X")

    if check_win(secret_word, old_letters_guessed):
        print("WIN")

    if num_of_tries == 6:
        print("LOSE")


# vacation.txt
main()
