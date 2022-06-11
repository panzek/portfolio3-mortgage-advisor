'''Handle import and banner'''

import pyfiglet

def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(title, font='banner3-D', width=90, justify='center')
    print(banner)

    print('Welcome to Mortgage Advisor Ireland!'.center(90))
    print('===================\n'.center(90))
    input('Please press any key to continue...'.center(90))

    print('\nAre you looking to buy a house in Ireland?')
    print('And you want to know the estimate of your monthly')
    print('repayments when you borrow to get a mortgage?\n')

   

    print('First create a username or Enter existing one.')
        