import math

# Explanation of the program
print("Password complexity, or entropy, can only truly be calculated by evaluating the randomness of the password generation method, not by analyzing the password itself.")

# Alphabet selection
print("The alphabet refers to the set of characters (or more generically, units) with which you assemble the password.")
# characters, or wordlist?
is_wordlist = input("Are you using a wordlist (for passphrases)? (Y/N): ")
if is_wordlist == "Y":
    wordlist_len = int(input("Enter the length of your wordlist: "))
    alphabet = wordlist_len
else:
    print("Select what you would like to include in your alphabet.")
    ab_len = 0
    lowercase = input("Include lowercase letters? (Y/N): ")
    uppercase = input("Include uppercase letters? (Y/N): ")
    numbers = input("Include numbers 0-9? (Y/N): ")
    special = input("Include these special characters?\n!@#$%^&*()_+-=`~,./;\'[]\\<>?:\"{}|\nThese are all the special characters available on a regular keyboard.\n (Y/N): ")

    if lowercase == "Y":
        ab_len += 26
    if uppercase == "Y":
        ab_len += 26
    if numbers == "Y":
        ab_len += 10
    if special == "Y":
        ab_len += 32
    print(f"Your alphabet has {ab_len} characters")
    alphabet = ab_len

# Letters
letters = int(input("Enter the number of selections from the alphabet (words for a passphrase, or characters in a password): "))

# Calculations
combination = alphabet ** letters
entropy = math.log2(combination)

# Output
print(f"Your password generation method can create {combination} possible passwords.")
print(f"This password selection method outputs passwords with {entropy:.2f} bits of entropy.")
