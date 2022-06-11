"""create user name"""
import gspread
from google.oauth2.service_account import Credentials
# from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENTS = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENTS.open('mortgage_advisor')

def user_name():
    """username function to get data from user"""

    while True:
        print('Username must be between 4 and 10 characters')
        print('Characters A-Z, a-z, 0-9 and spaces are permitted')
        print('Leading and trailing whitespaces will be removed\n')

        new_user = input('Please enter your username: \n').lower()

        if validate_username(new_user):
            print(f'{chr(10)}Thank you and welcome, {new_user}')
            break

    return new_user.strip()

def validate_username(new_user):
    """check username input to handle errors"""

    try:
        if not new_user:
            raise ValueError('You must enter a username')
        if len(new_user) < 4:
            raise ValueError(
                'Username must have at least 4 characters'
            )
        if len(new_user) > 10:
            raise ValueError(
                'Username must not exceed 10 characters'
            )

    except ValueError as error_msg:
        print(f'Invalid Data: {error_msg}, please try again{chr(10)}')
        return False

    return True
