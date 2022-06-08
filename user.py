"""create user name"""

def user_name():
    """username function to get data from user"""

    print('Username must be between 4 and 10 characters')
    print('Characters A-Z, a-z, 0-9 and spaces are permitted')
    print('Leading and trailing whitespaces will be removed\n')

    new_user = input('Please enter your username: ')
    print(f'Thank you and welcome, {new_user}')
