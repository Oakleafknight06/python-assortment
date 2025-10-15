import math
import string

def calc_entropy(alphabet_len, selections):
    """ Takes an integer 'alphabet_len' and an integer 'selections', and returns the number of possible combinations, and the entropy"""
    combination = pow(alphabet_len, selections)
    entropy = math.log2(combination)
    return combination, entropy

def create_alphabet(lowercase = False, uppercase = False, numbers = False, special = False, custom = None):
    """Boolean arguments: lowercase, uppercase, numbers, special. Also accepts a dictionary 'custom' for any other characters.
       If arguments are not supplied, they are assumed false/empty. """

    # Define variables
    ab_len = 0
    alphabet = set()

    # Processing
    if lowercase == True:
        alphabet = alphabet | set(string.ascii_lowercase)
    if uppercase == True:
        alphabet = alphabet | set(string.ascii_uppercase)
    if numbers == True:
        alphabet = alphabet | set(string.digits)
    if special == True:
        alphabet = alphabet | set(string.punctuation)
    if custom: # TODO If custom is a set or list, otherwise error
        alphabet = alphabet | set(custom)
        # TODO Make sure the mutable object does not persist between function calls.

    ab_len = len(alphabet)
    return ab_len, alphabet

def passphrase(wordlist, num_words, separation_char = "-", dice = False):
    print("unfinished")
    for i in num_words:
        # Get wordlist file
        if dice == True:
            # Ask the user for input from their dice
            print("oops, not implemented")
        else:
            # Generate random numbers
            print("oops, not implemented")
        
        # Pick word from wordlist, assign it to next_word
        user_passphrase = user_passphrase + separation_char + next_word
    return user_passphrase

