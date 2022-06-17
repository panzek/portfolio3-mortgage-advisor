'''Handle import and banner'''

import pyfiglet
from getch import getch, pause


def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(
        title, font='standard', width=80, justify='center'
        )
    print(banner)
    print('...A Mortgage Calculator Application!'.center(80))
    print('===================\n'.center(80))

    input('Please press any key to continue...\n')

    print('\nAre you looking to buy a house in Ireland?')
    print('And want to obtain an estimate of the monthly')
    print('repayments when you borrow to get a mortgage? Use')
    print('our mortgage calculator. First, enter a username\n')

    input('Press any key to continue...')

    return True
    
