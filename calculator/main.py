# Define the main calculator function
def calculator():
    # Prompt the user to select an operation
    operation = input('''select item calculator 
+ is jam
- is manfi
* is zarb
/ is taghsim
:''')

    # Addition operation
    if operation == '+':
        # Get two numbers from the user
        num1 = int(input('number1 :'))
        num2 = int(input('number2 :'))
        # Display the result of addition
        print(f'{num1} + {num2} = {num1 + num2}')

    # Subtraction operation
    elif operation == '-':
        # Get two numbers from the user
        num1 = int(input('number1 :'))
        num2 = int(input('number2 :'))
        # Display the result of subtraction
        print(f'{num1} - {num2} = {num1 - num2}')

    # Multiplication operation
    elif operation == '*':
        # Get two numbers from the user
        num1 = int(input('number1 :'))
        num2 = int(input('number2 :'))
        # Display the result of multiplication
        print(f'{num1} * {num2} = {num1 * num2}')

    # Division operation
    elif operation == '/':
        # Get two numbers from the user
        num1 = int(input('number1 :'))
        num2 = int(input('number2 :'))
        # Display the result of division
        print(f'{num1} / {num2} = {num1 / num2}')

    # Handle invalid operation input
    else:
        print('eshteb zadi!!!!!!')

    # Call the again function to ask if the user wants to continue
    again()


# Define the function to check if the user wants to continue
def again():
    # Prompt the user to continue or exit
    calculator_again = input('''
mekhay adameh bedy?(y/n)
:''')

    # If user chooses to continue, restart the calculator
    if calculator_again.upper() == 'Y':
        calculator()
    # If user chooses to exit, end the program
    elif calculator_again.upper() == 'N':
        return 'khodafes'
    # If input is invalid, call again function recursively
    else:
        again()


# Start the calculator for the first time
calculator()
