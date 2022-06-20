"""create user name"""
import sys
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from getch import pause
from welcome import welcome_intro
from print import print_red, print_green, print_yellow, print_cyan

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENTS = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENTS.open('mortgage_advisor')

first_time_buyer_sheet = SHEET.worksheet('first_time_buyer')


def user_name():
    """username function to get data from user"""

    while True:
        print('\nUsername must be between 4 and 10 characters')
        print('Characters A-Z, a-z, 0-9 and spaces are permitted')
        print('Leading and trailing whitespaces will be removed\n')

        username = input('Please enter a username: ').lower()

        if validate_username(username):
            check_username(username)
            get_user_data(username)

            break

    return username.strip()


def validate_username(username):
    """
    This will check if the username input
    data is valid or not, and will raise exception
    to handle any errors
    """

    try:
        if not username:
            raise ValueError('You must enter a username')
        if len(username) < 4:
            raise ValueError(
                'Username must have at least 4 characters'
            )
        if len(username) > 10:
            raise ValueError(
                'Username must not exceed 10 characters'
            )

    except ValueError as error_msg:
        print_red(f'{error_msg}, please try again')
        return False

    return True


def check_username(username):
    """
    Check if username exist and allow access to existing
    data. If there is no such username create a username
    """

    print_yellow(f'Checking "{username}" in database...')
    existing_user = first_time_buyer_sheet.find(username, in_column=1)

    while True:
        if existing_user:
            print_cyan(f'{chr(10)}Welcome back, {username}')
            sleep(3)
            try:
                print('Please choose one option: \033[1;33m1,2,or 3\033[00m')
                print('\033[1;33m1.\033[00m Retrieve mortgage results')
                print('\033[1;33m2.\033[00m Delete mortgage results')
                print('\033[1;33m3.\033[00m Exit the program')

                user_option = int(input(
                    'Enter your option: \033[1;33m1,2,or 3\033[00m: \n'
                    ))
                if user_option < 1 or user_option > 3:
                    sleep(1)
                    print_red('Enter a number between 1 and 3, try again!')
                    sleep(2)
                    continue

            except ValueError:
                sleep(1)
                print_red('Invalid Data: It needs to be a number, try again!')
                sleep(2)
                continue

            if user_option == 1:
                print_cyan('Retrieving mortgage calculator results...')
                sleep(3)
                print_green(f'Results retrieved successfully...{chr(10)}')
                get_user_data(username)

                pause(f'Press any key to return to options menu...{chr(10)}')
                return check_username(username)

            if user_option == 2:
                pause('\nPress any key to continue')
                print_cyan('Deleting saved mortgage calculation results...')
                sleep(3)

                first_time_buyer_sheet.delete_row(existing_user.row)
                print_red('Previous mortgage results deleted...')
                sleep(3)
                input('')

                return welcome_intro()

            if user_option == 3:
                pause('Press any key to continue')
                print_red('Exiting the application...')
                sleep(3)
                sys.exit(f'{chr(10)}Hey {username}, see you soon!')

        else:
            print_red(f'{username} not found...{chr(10)}')
            print_cyan('Creating your username...')

            sleep(3)

            print_green(
                f'Created username, "{username}" successfully!{chr(10)}'
                )
            validate_username(username)
            print_cyan(f'Welcome, {username}!')

            sleep(3)

        return existing_user


def get_user_data(username):
    """
    gets existing data if user is a returning visitor
    """
    existing_user = first_time_buyer_sheet.find(username, in_column=1)
    if existing_user:
        euro = chr(8364)
        property_value = first_time_buyer_sheet.row_values(
            existing_user.row
            )[1]
        loan_size = first_time_buyer_sheet.row_values(existing_user.row)[2]
        loan_term = first_time_buyer_sheet.row_values(existing_user.row)[3]
        monthly_repayment = first_time_buyer_sheet.row_values(
            existing_user.row
            )[4]
        print_yellow('RESULTS'.center(25))
        print('=========='.center(25))
        print(
            f'1. Property Value: \033[1;35m{euro}{property_value}\033[00m'
            )
        print(
            f'2. Loan Size: \033[1;35m{euro}{loan_size}\033[00m'
            )
        print(
            f'2. Loan Term: \033[1;35m{loan_term}yrs\033[00m'
            )
        print(
            f'4. Monthly Repayment:\033[1;35m{euro}{monthly_repayment}\033[00m'
            )
        print('==========\n'.center(25))
