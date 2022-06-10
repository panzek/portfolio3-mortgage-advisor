"""
specify scopes for access
obtain credentials using service account private key file
"""
import gspread
from google.oauth2.service_account import Credentials
import welcome
import menu
from user import user_name
from repayment import get_loan_data

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

def add_row_to_sheet(row):
    """ add row to worksheets"""
    first_time_buyer_sheet.append_row(row)

def main():
    """ 
    top level module to run  all program functions 
    """

welcome.welcome_intro()
user = user_name()
menu.menu_list()
loan_data = get_loan_data()
data = [ user, *loan_data]
add_row_to_sheet(data)

main()
