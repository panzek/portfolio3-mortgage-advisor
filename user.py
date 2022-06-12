"""create user name"""
import gspread
from google.oauth2.service_account import Credentials
import sys

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
        print('Username must be between 4 and 10 characters')
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
        # if username:
        #     raise ValueError(f'{chr(10)}{username} already taken')
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
        # input(f'{error_msg}. Are you a returning user?: y/n')
        print(f'Invalid Data: {error_msg}, please try again{chr(10)}')
        return False

    return True


def check_username(username):
    """
    Check if username exist and allow access to existing
    data. If there is no such username create a username
    """

    print(f'{chr(10)}Checking if {username} exist...{chr(10)}')
    existing_user = first_time_buyer_sheet.find(username, in_column=1)

    if existing_user:
        print(f'{username} already taken')

        make_choice = input(
            'Are you a returning user?: y/n '
            )
        if make_choice == 'y':
            print(f'{chr(10)}Welcome back, {username}')
            input('Press any key to retrieve existing mortgage results...\n')
        
        elif make_choice == 'n':
            input('Enter a different username')
            return username
            
    else:
        validate_username(username)
        print(f'{chr(10)}Welcome, {username}!')
    return True


def get_user_data(username):
    """
    gets existing data if user is a returning visitor
    """
    # get_data = first_time_buyer_sheet.get_all_values()
    # print(get_data)
    existing_user = first_time_buyer_sheet.find(username, in_column=1)
    if existing_user:
        euro = chr(8364)
        property_value = first_time_buyer_sheet.row_values(
            existing_user.row
            )[-4]
        loan_size = first_time_buyer_sheet.row_values(existing_user.row)[-3]
        loan_term = first_time_buyer_sheet.row_values(existing_user.row)[-2]
        monthly_repayment = first_time_buyer_sheet.row_values(
            existing_user.row
            )[-1]
        print('RESULTS'.center(25))
        print('=========='.center(25))
        print(f'1. Property Value: {euro}{property_value}')
        print(f'2. Loan Size: {euro}{loan_size}')
        print(f'3. Loan Term: {loan_term}yrs')
        print(f'4. Monthly Repayment: {euro}{monthly_repayment}')
        print('==========\n'.center(25))
    return True
# user_name()
