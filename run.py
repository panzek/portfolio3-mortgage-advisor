"""
specify scopes for access
obtain credentials using service account private key file
"""
import gspread
from google.oauth2.service_account import Credentials
import welcome
import user
import menu

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENTS = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENTS.open('mortgage_advisor')

welcome.welcome_intro()
user.user_name()
menu.menu_list()
