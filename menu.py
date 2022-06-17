""" Options menu """
import sys
import time
from google.oauth2.service_account import Credentials


def menu_list():
    """
    List of options
    This will also check if the username input
    data is valid or not, and will raise exception
    to handle any errors
    """

    while True:
        try:
            print('Please choose one of the following options:')
            print('1. Run an overview of this application')
            print('2. Run mortgage calculator')
            print('3. Exit the application')

            list_option = int(input(f'{chr(10)}Please enter your choice: 1,2, or 3:{chr(10)}'))
            # validate input
            if list_option < 1 or list_option > 5:
                time.sleep(1)
                print('Enter a number between 1 and 5, try again!\n')
                time.sleep(2)
                continue

        except ValueError:
            time.sleep(1)
            print('It needs to be a number, try again!\n')
            time.sleep(2)
            continue

        else:
            break

    check_menu_list(list_option)


def check_menu_list(list_option):
    """ handle user inputs and errors"""

    if list_option == 1:
        print('\nOur Application Overview')
        print('==================')
        print('\nOur application gives First Time Buyers (FTB)')
        print('an estimate of their monthly repayments when')
        print('they borrow to get a mortgage, depending on the amount')
        print('borrowed, interest rate, and the mortgage term.\n')

        input('Press any key to continue... \n')

        print('Estimate your mortgage repayments by ')
        print('entering your property price, how ')
        print('much you would like to borrow ')
        print('and over what period (loan term).\n')

        input('Press any key to continue... \n')

        print('an overview of the new mortgage')
        print('lending in Ireland as published by the')
        print('Central Bank of Ireland in 2022 and estimates.')
        print('the user monthly repayments.\n')

        input('Press any key to return to main menu... \n')

        menu_list()

    elif list_option == 2:
        print('Mortgage Calculator'.center(25))
        print('=================='.center(25))
        print('\nThis mortgage calculator is for')
        print('First Time Buyer (FTB) only\n')

        time.sleep(2)

    elif list_option == 3:
        print('exiting the program')
        time.sleep(3)
        sys.exit("Exited successfully, thanks for looking in!")

    else:
        return True
