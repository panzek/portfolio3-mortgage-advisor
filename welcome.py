'''Handle import and banner'''

import pyfiglet
from getch import getch, pause
from print import print_yellow


def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(
        title, font='standard', width=80, justify='center'
        )
    print(banner)
    print_yellow('...A Mortgage Calculator Application!'.center(80))
    print('===================\n'.center(80))

    pause('\033[1;36mPlease press any key to continue...\033[00m')

    print('\nAre you looking to buy a house in Ireland?')
    print('And you want to obtain an estimate of the monthly')
    print('repayments when you borrow to get a mortgage? To use')
    print('our mortgage calculator, first enter a username\n')

    pause('\033[1;36mPlease press any key to continue...\033[00m')

    return True
