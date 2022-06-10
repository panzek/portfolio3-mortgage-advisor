'''Handle import and banner'''

import pyfiglet

def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(title, font='banner3-D', width=90, justify='center')
    print(banner)

    print('Hi, and Welcome!\n')
    print('Are you looking to buy a house in Ireland?')
    print('And you want to know the estimate of your monthly')
    print('repayments when you borrow to get a mortgage?\n')

    input('Please press any key to start...\n')

    print('First create a username or Enter existing one.')
        