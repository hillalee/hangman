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

    from functions import (opening, choose_word, check_win, check_valid_input, show_hidden_word,
                            try_update_letter_guessed, photos)
    print(opening)
    # ask user for file path an index
    file_path = input("insert file path: ")
    index = int(input("Insert an index: "))
    secret_word = choose_word(file_path, index)  # chooses a word

    print(HANGMAN_PHOTOS[num_of_tries])

    # work
    while num_of_tries < 6:
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input("Insert a letter: ")

        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if not check_valid_input(letter_guessed, old_letters_guessed):
            print(letter_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
        print(old_letters_guessed)

        if letter_guessed in old_letters_guessed:
            num_of_tries += 1
            print("):")
            print(HANGMAN_PHOTOS[num_of_tries])




    if num_of_tries == 6:
        print("LOSE")


# vacation.txt

main()
