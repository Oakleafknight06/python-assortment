import math

# TODO: Rewrite program as a module with function definitions

def calc_entropy(alphabet, letters)
    combination = alphabet ** letters
    entropy = math.log2(combination)
    return entropy

def create_alphabet()


def passphrase(wordlist, dice_list)
# eg 7776 long list and/or text file, [1, 3, 4, 6, 6, 2]





if __name__ == __main__
    # Explanation of the program
    print("Password entropy, or randomness, can only truly be calculated by evaluating the randomness of the password generation method, not by analyzing the password itself.")

    # Alphabet selection
    print("\n****** Alphabet Selection *****\n\nThe alphabet refers to the set of characters or words with which you assemble the password.")
    # characters, or wordlist?
    is_wordlist = input("Are you using a wordlist (ie making a passphrases)? (y/N): ")
    if is_wordlist == ("Y" or "y"):
        wordlist_len = int(input("\nEnter the length of your wordlist: "))
        alphabet = wordlist_len
    else:
        print("\nOkay, starting alphabet selection process.\nSelect what you would like to include in your alphabet.")
        ab_len = 0

        lowercase = input("Include lowercase letters? (y/N): ")
        if lowercase == ("Y" or "y"):
            ab_len += 26
        else:
            print("Not including lowercase letters")

        uppercase = input("Include uppercase letters? (y/N): ")
        if uppercase == ("Y" or "y"):
            ab_len += 26
        else:
            print("Not including uppercase letters")

        numbers = input("Include numbers 0-9? (y/N): ")
        if numbers == ("Y" or "y"):
            ab_len += 10
        else:
            print("Not including numbers")

        special = input("Include these special characters?\n!@#$%^&*()_+-=`~,./;\'[]\\<>?:\"{}|\nThese are all the special characters available on a regular keyboard.\n (y/N): ")
        if special == ("Y" or "y"):
            ab_len += 32
        else:
            print("Not including special characters")

        print(f"\nYour alphabet has {ab_len} characters")
        alphabet = ab_len

    # Letters
    letters = int(input("\nEnter the number of selections from the alphabet (words for a passphrase, or characters in a password): "))

    # Calculations
    # Output
    print(f"Your password generation method can create {combination} possible passwords.")
    print(f"This password selection method outputs passwords with {entropy:.2f} bits of entropy.")
