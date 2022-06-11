"""create user name"""
import gspread
from google.oauth2.service_account import Credentials

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

        username = input('Please enter your username: ').lower()

        if validate_username(username):
            check_username(username)

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

    print(f'{chr(10)}Checking if {username} exist...')
    existing_user = first_time_buyer_sheet.find(username, in_column=1)

    if existing_user:
        print(f'{chr(10)}Welcome back, {username}')
    else:
         validate_username(username)
         print(f'{chr(10)}Thank you and welcome, {username}')

user_name()
