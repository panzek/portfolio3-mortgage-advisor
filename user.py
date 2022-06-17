"""create user name"""
import sys
import time
import gspread
from google.oauth2.service_account import Credentials
from welcome import welcome_intro

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
        print(f'Invalid Data: {error_msg}, please try again{chr(10)}')
        return False

    return True


def check_username(username):
    """
    Check if username exist and allow access to existing
    data. If there is no such username create a username
    """

    print(f'Checking {username} in database...')
    existing_user = first_time_buyer_sheet.find(username, in_column=1)

    while True:
        if existing_user:
            print(f'{chr(10)}Welcome back, {username}')
            try:
                print('\nPlease choose one option: 1,2,or 3')
                print('1. Retrieve mortgage results')
                print('2. Delete mortgage results')
                print('3. Exit the program')

                user_option = int(input('Please enter your option: 1,2,or 3: \n'))
                if user_option < 1 or user_option > 3:
                    time.sleep(1)
                    print('Enter a number between 1 and 3, try again!')
                    time.sleep(2)
                    continue

            except ValueError:
                time.sleep(1)
                print('It needs to be a number, try again!')
                time.sleep(2)
                continue

            if user_option == 1:
                print('\nRetrieving mortgage calculator results...')
                time.sleep(3)
                print(f'Results retrieved successfully...{chr(10)}')
                get_user_data(username)

                input(f'Press any key to return to options menu...{chr(10)}')

            if user_option == 2:
                delete_program = input(
                    '\nDo you really want to delete previous mortgage results?: y/n\n'
                    ).lower()
                if delete_program in ('y', 'yes'):
                    input(f'{chr(10)}Press {delete_program} again to confirm...')
                    print(f'{chr(10)}Deleting previous mortgage results...')

                    time.sleep(3)

                    first_time_buyer_sheet.delete_row(existing_user.row)
                    input(f'{chr(10)}Previous mortgage results deleted...')

                    return welcome_intro()

            if user_option == 3:
                quit_program = input(
                    '\nDo you really want to exit progam?: y/n'
                    ).lower()
                if quit_program in ('y', 'yes'):
                    input(f'Press {quit_program} again to confirm...')
                    print(f'{chr(10)}Exiting the application...')

                    time.sleep(3)

                    sys.exit(f'{chr(10)}{username}, see you soon!')

                if quit_program in ('n', 'no'):
                    return user_option

        else:
            print(f'{chr(10)}{username} not found...{chr(10)}')
            print('Creating your username...')

            time.sleep(3)

            print(f'Created username, {username} successfully!{chr(10)}')
            validate_username(username)
            print(f'Welcome, {username}!')

            time.sleep(3)

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
        print('RESULTS'.center(25))
        print('=========='.center(25))
        print(f'1. Property Value: {euro}{property_value}')
        print(f'2. Loan Size: {euro}{loan_size}')
        print(f'3. Loan Term: {loan_term}yrs')
        print(f'4. Monthly Repayment: {euro}{monthly_repayment}')
        print('==========\n'.center(25))

    return True
