""" Options menu """
import sys
from time import sleep
from getch import getch, pause
from google.oauth2.service_account import Credentials
from print import print_yellow, print_red


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
            print('\033[1;33m1.\033[00m Run an overview of this application')
            print('\033[1;33m2.\033[00m Run mortgage calculator')
            print('\033[1;33m3.\033[00m Exit the application')

            list_option = int(input(f'Enter your choice: \033[1;33m1,2,or 3\033[00m:{chr(10)}'))
            # validate input
            if list_option < 1 or list_option > 5:
                sleep(1)
                print('Enter a number between 1 and 5, try again!\n')
                sleep(2)
                continue

        except ValueError:
            sleep(1)
            print('It needs to be a number, try again!\n')
            sleep(2)
            continue

        else:
            break

    check_menu_list(list_option)


def check_menu_list(list_option):
    """ handle user inputs and errors"""

    if list_option == 1:
        print('Our Application Overview'.center(35))
        print_yellow('=================='.center(35))
        print('Our application gives First Time Buyers (FTB)')
        print('an estimate of their monthly repayments when')
        print('they borrow to get a mortgage, depending on the amount')
        print('borrowed, interest rate, and the mortgage term.\n')

        pause('Press any key to continue... \n')

        print('Estimate your mortgage repayments by ')
        print('entering your property price, how ')
        print('much you would like to borrow ')
        print('and over what period (loan term).\n')

        pause('Press any key to continue... \n')

        print('an overview of the new mortgage')
        print('lending in Ireland as published by the')
        print('Central Bank of Ireland in 2022 and estimates.')
        print('the user monthly repayments.\n')

        pause('Press any key to return to new user menu...')
        sleep(2)
        print_yellow('Returning your to new user menu... \n')
        sleep(3)

        menu_list()

    elif list_option == 2:
        print_yellow('Mortgage Calculator'.center(25))
        print('=================='.center(25))
        print('This mortgage calculator is for')
        print('First Time Buyer (FTB) only\n')

        sleep(2)

    elif list_option == 3:
        print_red('exiting the program')
        sleep(3)
        sys.exit('\033[1;32mExited successfully, thanks for looking in!\033[00m')

    else:
        return True
