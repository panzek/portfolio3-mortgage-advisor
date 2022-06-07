'''Handle import and banner'''
import pyfiglet 
def welcome_intro():

    '''Welcome message and introduction'''

    title = 'Mortgage Advisor'
    banner = pyfiglet.figlet_format(title, font='banner3-D', width=90, justify='center')
    print(banner)

    print('Welcome to your Mortgage Advisor!'.center(90))
    print('============================\n'.center(90))
    print('Are you looking to buy a house in Ireland?')
    print('And you are a First Time Buyer (FTB)')
    print('or a Second & Subsequent Buyer (SSB)?')
    print('And wants to know the estimate of your monthly')
    print('repayments when you borrow to get a mortgage?\n')
    print('First, introduce yourself.\n')
    