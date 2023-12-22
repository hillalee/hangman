def check_valid_input(letter_guessed, old_letters_guessed):
    """this function returns if letter_guessed is one english letter and wasn't guessed already
    :param letter_guessed: the letter guessed by user
    :param old_letters_guessed: old letters the user already guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: bool of weather the letter is right or not
    :rtype: bool"""
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or (not letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed):
        return False
    else:
        return True


print(check_valid_input('A',['a', 'b', 'c']))
