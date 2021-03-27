# Imports
import random
import string
from time import sleep


print("\nYou are using the \"Password Generator v2.0\" made by LotusXvr")
sleep(2)


# Listing the primary alphabet for later adictions
lower_alphabet = list(string.ascii_lowercase)
characters = lower_alphabet


# Input of X characters from list
while True:
    try:
        print("\nHow many characters would you like your password to have?")
        quantity_of_characters = int(input("Amount of characters: "))

        while quantity_of_characters <= 2:
            print("Your password should be more then 2 characters long, right? Try again!")
            quantity_of_characters = int(input("Amount of characters: "))

        break
    
    except:
        print("\nInput should be a number")
        continue
    

# Input if they want uppercase letters
upper_alphabet = list(string.ascii_uppercase)
uppercase_bool = False

while True:
    print("\nDo you want uppercase letters on your password?")
    want_uppercase = str(input("y/1 for yes (or) n/2 for no: "))
    if want_uppercase in "yY1":
        characters.extend(upper_alphabet)
        print("Uppercase letters: Yes")
        uppercase_bool = True
        break
    if want_uppercase in "nN2":
        print("Uppercase letters: No")
        break
    else:
        print("\nInvalid input")
        continue


# Input if they want numbers
numbers = ["1","2","3","4","5","6","7","8","9","0"]
numbers_bool = False

while True:
    print("\nDo you want numbers on your password?")
    want_numbers = str(input("y/1 for yes (or) n/2 for no: "))
    if want_numbers in "yY1":
        characters.extend(numbers)
        print("Numbers: Yes")
        numbers_bool = True
        break
    if want_numbers in "nN2":
        print("Numbers: No")
        break
    else:
        print("\nInvalid input")
        continue


# Input if they want Special Characters
special_characters = ["@", "_", "#", "!", "?", "$", ".", ",", "&", "(", ")", "[", "]", "{", "}", ":", "+", "^", "~", "*", "="]
special_bool = False

while True:
    print("\nDo you want special characters on your password?")
    want_special = str(input("y/1 for yes (or) n/2 for no: "))
    if want_special in "yY1":
        characters.extend(special_characters)
        print("Special characters: Yes")
        special_bool = True
        break
    if want_special in "nN2":
        print("Special characters: No")
        break
    else:
        print("\nInvalid input")
        continue


# Input of X amount of passwords
while True:
    try:
        print("\nHow many passwords would you like?")
        quantity_of_passwords = int(input("Amount of passwords: "))

        while quantity_of_passwords == 0:
            print("You should want more then zero passwords, right? Try again!")
            quantity_of_passwords = int(input("Amount of passwords: "))
        
        break

    except:
        print("\nInput should be a number")
        continue


# Multiplying the list for more characters and variety
for multiplication in range(10):
    characters.extend(characters)


# The Output
# Listing the passwords
password_number = 1

# Receipt
print("\n- Your request was:")
print(f"{quantity_of_passwords} passwords with {quantity_of_characters} characters")
print("- Details:")
print("Lowercase: Default")
if uppercase_bool:
    print("Uppercase: Selected")
else:
    print("Uppercase: Not selected")
if numbers_bool:
    print("Numbers: Selected")
else:
    print("Numbers: Not Selected")
if special_bool:
    print("Special: Selected")
else:
    print("Special: Not selected")
sleep(5)

# Proceed?
while True:    
    print("\nDo you want to proceed?")
    proceed = str(input("y/1 for yes (or) n/2 for no: "))

    if proceed in "yY1":

        if quantity_of_passwords == 1:
            print("\nYour password is:")
        if quantity_of_passwords >= 2:
            print("\nYour passwords are:")

        for password in range(quantity_of_passwords):
            sleep(0.01)
            # Shuffling all characters and grabbing the quantity of characters from the list
            random.shuffle(characters)
            password_characters = random.sample(characters, quantity_of_characters)
            # Shuffling the X characters and joining the list to a single string
            random.shuffle(password_characters)
            password_shuffled = ''.join(password_characters)
            # Printing the result
            print(f"({password_number})", password_shuffled)
            password_number += 1

        print("\nEnd of program.")
        break

    if proceed in "nN2":
        print("\nProgram terminated by user input.")
        break

    else:
        print("\nInvalid input")
        continue
    
    






