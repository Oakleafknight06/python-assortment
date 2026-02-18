import math
import string

def calc_comb(alphabet_len: int, selections: int) -> int:
    return pow(alphabet_len, selections)

def calc_entropy(combinations: int) -> int:
    return math.log2(combinations)

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

## TODO

def dict_check(passphrase: str) -> str:
    """check passphrase against wordlists, return warning if common/vulnerable."""
    # Also is dictionary check, etc
    # breach list check
    # dict check
    ...

def pattern_analzye(passphrase: str) -> str:
    """Attempt to pattern analyze user provided (not program-generated) passphrase and print guesses. For example, figure out if is a passphrase, search wordlists and guess which one was used, attempt to guess entropy. Basically a password cracker, need to look into how those work. Also, detect years, pet names, place names, English words in non passphrase passwords, etc."""

def gen_passphrase(wordlist, num_words, separation_char = "-", dice = False):
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
    # Check password entropy against NIST guidelines in main. Check if is lower, and warn. If above, say is good based on NIST minimum
    # https://pages.nist.gov/800-63-4/sp800-63b.html#password
    # Minimum of 15 characters
    pass
