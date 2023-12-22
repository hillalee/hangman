def photos():
    HANGMAN_PHOTOS = {1: '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 2: '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', 3: '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', 4: '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', 5: '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', 6: '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', 7: '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''}


def opening():
    MAX_TRIES = 6
    print("""Welcome to the game Hangman\n""" +
          """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/""" + "\n", MAX_TRIES)


opening()


def check_win(secret_word, old_letters_guessed):
    """this function returns what the user has done so far"""
    secret_word = list(secret_word)
    current_situation = list("_" * len(secret_word))
    for char in old_letters_guessed:
        for i in range(len(secret_word)):
            if char == secret_word[i]:
                current_situation[i] = char
    print("".join(current_situation))
    print(str(current_situation).isalpha())
    print(len(current_situation))
    if str(current_situation).isalpha():
        return True
    else:
        return False



def show_hidden_word(secret_word, old_letters_guessed):
    """Displays guessed letters in the secret word, and '_' for letters that were
    not guessed yet"""
    result = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            result = result + letter + ' '
        else:
            result = result + "_ "
    print(result[:-1])


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function returns if letter_guessed is one english letter and wasn't guessed already"""
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or (not letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function returns if letter_guessed is one english letter and
    wasn't guessed already, also returns X if the letter is false and a list
    of letters already guessed"""
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or (not letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.extend(letter_guessed)
        return True


def choose_word(file_path, index):
    """choose a secret word for the player!
        returns number of possible words and an index"""

    with open(file_path, "r") as file:
        # make a list of words
        text = file.read()
        text = text.replace("\n", "")
        words = text.split(" ")  # list of words

        #  count how many words
        how_many = []
        for word in words:
            if word not in how_many:
                how_many.append(word)

        # find index
        word_index = words[index % len(words) - 1]

        return word_index
