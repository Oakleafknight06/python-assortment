import math
import string

def calc_entropy(alphabet_len, selections):
    """ Takes an integer 'alphabet_len' and an integer 'selections', and returns the number of possible combinations, and the entropy"""
    combination = pow(alphabet_len, selections)
    entropy = math.log2(combination)
    return combination, entropy

def create_alphabet(lowercase = False, uppercase = False, numbers = False, special = False):
    """Boolean arguments: lowercase, uppercase, numbers, special. If arguments are not supplied, they are assumed False. """

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

    return alphabet

def passphrase(wordlist, num_words, separation_char = "-", dice = False):
    user_list = []
    prog_list = []
    with open(wordlist) as wordfile:
    print(prog_list)

    for i in range(num_words):
        # Get wordlist file. Open file based on path provided by user? Or offer options/include only own file..
        if dice == True:
            # Ask the user for input from their dice
            print("oops, not implemented")
        else:
            # Generate random numbers
            print("oops, not implemented")
        
        # Pick word from wordlist, assign it to next_word
        user_list.append(next_word)
    user_passphrase = separation_char.join(user_list)
    return user_passphrase

if __name__ == "__main__":
    passphrase("orchard-street-medium.txt", 4)
