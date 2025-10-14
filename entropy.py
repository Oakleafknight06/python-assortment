import math

def calc_entropy(alphabet, selections):
    combination = pow(alphabet, selections)
    entropy = math.log2(combination)
    return entropy

def create_alphabet(lowercase = False, uppercase = False, numbers = False, special = False, custom = []):
    # TODO: First four variables are boolean, last is a list and is optional. If arguments are not supplied, it is assumed false.
    # TODO: Also return a list of the characters in the alphabet, rather than just the length

    # Define variables
    ab_len = 0
    alphabet = set()
    special_charset = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "`", "~", ",", ".", "/", ";", "'", "[", "]" "\\", "<", ">", "?", ":", "\"", "{", "}", "|"}

    if lowercase == True:
        ab_len += 26

    if uppercase == True:
        ab_len += 26

    if numbers == True:
        ab_len += 10

    if special == True:
        ab_len += 32
        alphabet = alphabet.union(special_charset)

    if custom:
        ab_len += len(custom)

    # return alphabet
    # how to return two things?
    return ab_len

def passphrase(wordlist, dice_list):
    print("unfinished")
    # eg 7776 long list and/or text file, [1, 3, 4, 6, 6, 2]
    # Get wordlist file
    # Ask for number of words from user
    # Ask if user wants to roll dice or use system randomness
    # Pick words from wordlist, repeat for as many words needed
    # Return passphrase

