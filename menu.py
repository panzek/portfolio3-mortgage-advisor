""" Options menu """

def menu_list():
    """ List of options """

    while True:
        print('\nPlease choose one of the following options:')
        print('\n1. To run an overview of this application')
        print('2. To run through the instructions')
        print('3. To run new mortgage enquiry')
        print('4. To delete existing mortgage enquiry results')
        print('9. To exit the application\n')

        list_option = int(input('Please enter your option: 1,2,3,4, or 9: \n'))
        check_menu_list(list_option)

def check_menu_list(list_option):
    """ handle user inputs and errors"""

    if list_option == 3:
        print('\nPlease select your mortgage type: 1 or 2')
        print('1. First Time Buyer (FTB)')
        print('2. Second & Subsequent Buyer (SSB)\n')

        int(input('Please enter your option: \n'))
