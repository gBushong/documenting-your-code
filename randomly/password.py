from typing import Optional, Iterable
import random
import string


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable] = []) -> str:
    """This function creates and outputs a random password.

    Parameters
    ----------
    chars: int
        number of characters required for output password
    punctuation: bool
        T/F for whether punctuation is required in output password
    invalid_chars: Optional[Iterable] = None
        optional arg, defaults to None
        list of invalid characters for output password

    Returns
    -------
    string:
        randomly generated password of specified num chars, with/without punc,
        excluding invalid chars
    """

    # create list of all letters and digits
    valid_chars = string.ascii_letters + string.digits

    # add punctuation if desired
    if punctuation:
        valid_chars += string.punctuation

    # remove any invalid chars
    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # generate random list of chars of correct length & 
    # join into string
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
