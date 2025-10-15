import math
import string

def calc_entropy(alphabet_len, selections):
    """ Takes an integer 'alphabet_len' and an integer 'selections', and returns the number of possible combinations, and the entropy"""
    combination = pow(alphabet_len, selections)
    entropy = math.log2(combination)
    return combination, entropy

def create_alphabet(lowercase = False, uppercase = False, numbers = False, special = False, custom = None):
    """Boolean arguments: lowercase, uppercase, numbers, special. Also accepts a dictionary 'custom' for any other characters.
       If arguments are not supplied, they are assumed false/empty.
    """

    # Define variables
    ab_len = 0
    alphabet = set()
    special_charset = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "`", "~", ",", ".", "/", ";", "'", "[", "]" "\\", "<", ">", "?", ":", "\"", "{", "}", "|"}

    # Processing
    if lowercase == True:
        ab_len += 26
        alphabet = alphabet | set(string.ascii_lowercase)

    if uppercase == True:
        ab_len += 26
        alphabet = alphabet | set(string.ascii_uppercase)

    if numbers == True:
        ab_len += 10
        alphabet = alphabet | set(string.digits)

    if special == True:
        ab_len += 32
        alphabet = alphabet | special_charset

    if custom: # TODO If custom is a set or list, otherwise error
        ab_len += len(custom)
        alphabet = alphabet | set(custom)
        # TODO Make sure the mutable object does not persist between function calls.

    return ab_len, alphabet

def passphrase(wordlist, dice_list):
    print("unfinished")
    # eg 7776 long list and/or text file, [1, 3, 4, 6, 6, 2]
    # Get wordlist file
    # Ask for number of words from user
    # Ask if user wants to roll dice or use system randomness
    # Pick words from wordlist, repeat for as many words needed
    # Return passphrase

