# تمرین شماره 1
# برنامه ای بنویسید که از کاربر تاریخ امروز رو بگیرد به صورت (روز ماه سال )
# استفاده از def

from colorama import Fore

# Display the message to the user
message = "Hello my friend! Welcome to this program. To start, just enter today's date to see the result!!!"
print(f'{message[:17]}\n{message[17:]}')


# Definition of date conversion function
def date_conversion(x):
    # If the date is less than 1400, it will show this message
    if int(x[0]) < 1400:
        print(Fore.RED + 'This program works for dates after 1400!!!')
        return

    # If the month is greater than 12 or less than 1, it displays an error
    if int(x[1]) > 12 or int(x[1]) < 1:
        print(Fore.RED + 'You entered the wrong month!!!')
        return

    # Otherwise, it will display the date in the desired format
    print(f'Date: ({x[0]}/{x[1]}/{x[2]})')


# Instruction to the user
print(Fore.YELLOW + '''
Note: Enter The Date In This Format >>> 1400 12 29
''')

# Getting date from user
user_input = input('Enter The Date: ').split(' ')

# Try-except block to handle input errors
try:
    # Attempt to convert inputs to integers
    user_input = list(map(int, user_input))

    # Call the date conversion function
    date_conversion(user_input)

except (IndexError, ValueError):
    print(Fore.RED + 'You entered the date wrongly or too few values!!!')


