# import library
import random
import string


lower = string.ascii_lowercase

upper = string.ascii_uppercase

symbol = string.punctuation

digit = string.digits

all = lower + upper + symbol + digit



while True:
    try:
        print('''\nchoose your Option
        1)create password
        2)Exit''')
        choose = input('your choice:')

        if choose == '1':

            length = int(input('set password lenght :'))

            password = ''.join(random.sample(all, length))

            print(f'New password: {password}')

        elif choose == '2':
            break
        else:
            print('choose your option wrong!!!')
    except ValueError:

        print('The password is too long!')