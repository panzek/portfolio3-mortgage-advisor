""" Options menu """
import sys
import time
from google.oauth2.service_account import Credentials


def menu_list():
    """ List of options """

    while True:
        print('Please choose one of the following options:')
        print('1. Run an overview of this application')
        print('2. Run through the instructions')
        print('3. Run mortgage calculator')
        print('4. Get existing mortgage calculator results')
        print('5. Exit the application')

        list_option = int(input('Please enter your option: 1,2,3,4, or 5: \n'))
        check_menu_list(list_option)

        return menu_list


def validate_list(list_option):
    """
    This will check if the username input
    data is valid or not, and will raise exception
    to handle any errors
    """

    try:
        if list_option == "":
            raise ValueError('You must enter a value')
        if list_option < 0:
            raise ValueError(
                'Username must have at least 4 characters'
            )
        if list_option > 5:
            raise ValueError(
                'Username must not exceed 5 characters'
            )

    except ValueError as error_msg:
        print(f'Invalid Data: {error_msg}, please try again{chr(10)}')
        return False

    return True

def check_menu_list(list_option):
    """ handle user inputs and errors"""

    if list_option == 1:
        print('\nOur Application Overview')
        print('==================')
        print('\nOur application will show how much your')
        print('mortgage repayment will cost you')
        print('when you borrow to get a mortgage,')
        print('depending on the amount you borrow,')
        print('interest rate, and the mortgage term.\n')

        input('Press any key to continue... \n')

        print('It gives the user, either as a First Time')
        print('Buyer (FTB) or a Second and Subsequent')
        print('Buyer (SSB) an overview of the new mortgage')
        print('lending in Ireland as published by the')
        print('Central Bank of Ireland in 2022 and estimates.')
        print('the user monthly repayments.\n')
        input('Press any key to return to main menu... \n')

    elif list_option == 2:
        print('\nInstructions')
        print('==================\n')
        print('How to use our mortgage calculator?\n')
        print('To start, choose your mortgage type:')
        print('First Time Buyer (FTB) or')
        print('Second & Subsequent Buyer (SSB)\n')

        input('Press any key to continue... \n')

        print('How much will the repayments be?\n')
        print('Estimate your mortgage repayments by ')
        print('entering your property price, how ')
        print('much you would like to borrow ')
        print('and over what period (loan term).\n')

        input('Press any key to return to main menu... \n')

    elif list_option == 3:
        print('\nPlease select your mortgage type: 1 or 2')
        print('1. First Time Buyer (FTB)')
        print('2. Second & Subsequent Buyer (SSB)\n')

        int(input('Please enter your option: \n'))

    elif list_option == 4:
        existing_result = input(
            '\nGet existing mortgage calculator results: y/n? '
            ).lower()
        confirm_result = input(
            f'Press {existing_result} again to confirm: '
            ).lower()

        if existing_result == confirm_result:
            print('Hello World!')

        else:
            print('No Match!')
            input(f'Press {existing_result} again to confirm: ').lower()
            # quit()

    elif list_option == 5:
        print('exiting the program')
        time.sleep(3)
        sys.exit("You exit the program, thanks for looking in!")
    
    else:
        validate_list(list_option)