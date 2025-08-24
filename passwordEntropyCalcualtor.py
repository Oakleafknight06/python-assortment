import math

alphabet = int(input("What is the alphabet size: "))
letters = int(input("How many selections from the alphabet: "))
combination = alphabet ** letters
entropy = math.log2(combination)
roundedEntropy = round(entropy, 3)
print(combination, " is the number of possible combinations")
print("This password selection method outputs passwords with " + str(roundedEntropy) + " bits of entropy.")
