'''Handle import and banner'''

import pyfiglet
from getch import getch, pause


def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(
        title, font='standard', width=60, justify='center'
        )
    print(banner)

    print('Welcome to Mortgage Advisor Ireland!'.center(60))
    print('===================\n'.center(60))
    pause(input('Please press any key to continue...'))

    print('\nAre you looking to buy a house in Ireland?')
    print('And you want to know the estimate of your monthly')
    print('repayments when you borrow to get a mortgage?')
    print('First, create a username or Enter existing one.\n')

    input('Press any key to continue...')

    return True
    
