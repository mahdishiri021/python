# Import necessary libraries
import random
import string

# Define character sets for password generation
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
digit = string.digits

# Combine all character sets into one
all = lower + upper + symbol + digit

# Start an infinite loop to keep the program running
while True:
    try:
        # Display options to the user
        print('''\nchoose your Option
        1)create password
        2)Exit''')
        choose = input('your choice:')  # Get user's choice

        if choose == '1':
            # If user chooses to create a password
            length = int(input('set password length :'))  # Get desired password length from user

            # Generate a random password of the specified length
            password = ''.join(random.sample(all, length))

            # Display the generated password
            print(f'New password: {password}')

        elif choose == '2':
            # If user chooses to exit
            break
        else:
            # If user enters an invalid option
            print('choose your option wrong!!!')
    except ValueError:
        # Handle the case where the user enters a non-integer value for password length
        print('The password is too long!')