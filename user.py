"""create user name"""

def user_name():
    """username function to get data from user"""

    while True:
        print('Username must be between 4 and 10 characters')
        print('Characters A-Z, a-z, 0-9 and spaces are permitted')
        print('Leading and trailing whitespaces will be removed\n')

        new_user = input('Please enter your username: ')

        if check_username(new_user):
            print(f'Thank you and welcome, {new_user}')
            break

        return user_name

def check_username(new_user):
    """check username input to handle errors"""

    try:
        if not new_user:
            raise ValueError('You must enter a username')
        if len(new_user) < 4 or len(new_user) > 10:
            raise ValueError(
                f'Characters between 4 & 10 required, you entered {len(new_user)}'
            )

    except ValueError:
        print('No username entered, please try again')
        print('invalid data: {new_user}, please try again')
        return False

    return True
