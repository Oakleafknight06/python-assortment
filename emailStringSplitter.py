email = input("Please input the email: ")
atPos = email.index("@")
atPosPlusOne = atPos + 1
username = email[0:atPos].lower()
domain = email[atPosPlusOne:].lower()
print("The user is", username)
print("The email domain is", domain)
