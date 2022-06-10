""" Options menu """

def menu_list():
    """ List of options """

    while True:
        print('\nPlease choose one of the following options:')
        print('\n1. To run an overview of this application')
        print('2. To run through the instructions')
        print('3. To run new mortgage enquiry')
        print('4. To delete existing mortgage enquiry results')
        print('5. To exit the application\n')

        list_option = int(input('Please enter your option: 1,2,3,4, or 5: \n'))
        check_menu_list(list_option)

        return menu_list

def check_menu_list(list_option):
    """ handle user inputs and errors"""

    if list_option == 1:
        print('\nOur Application Overview')
        print('==================')
        print('\nOur application will show how much your')
        print('mortgage repayment will cost you')
        print('when you borrow to get a mortgage,')
        print('depending on the amount you borrow,')
        print('interest rate, and the mortgage term.\n')

        input('Press any key to continue... \n')

        print('It gives the user, either as a First Time')
        print('Buyer (FTB) or a Second and Subsequent')
        print('Buyer (SSB) an overview of the new mortgage')
        print('lending in Ireland as published by the')
        print('Central Bank of Ireland in 2022 and estimates.')
        print('the user monthly repayments.\n')

        input('Press any key to return to main menu... \n')

    if list_option == 2:
        print('\nInstructions')
        print('==================\n')
        print('How to use our mortgage calculator?\n')
        print('To start, choose your mortgage type:')
        print('First Time Buyer (FTB) or')
        print('Second & Subsequent Buyer (SSB)\n')

        input('Press any key to continue... \n')

        print('How much will the repayments be?\n')
        print('Estimate your mortgage repayments by ')
        print('entering your property price, how ')
        print('much you would like to borrow ')
        print('and over what period (loan term).\n')

        input('Press any key to return to main menu... \n')

    if list_option == 3:
        print('\nPlease select your mortgage type: 1 or 2')
        print('1. First Time Buyer (FTB)')
        print('2. Second & Subsequent Buyer (SSB)\n')

        int(input('Please enter your option: \n'))
        # mortgage_type = int(input('Please enter your option: \n'))
        # if list_option.mortgage_type:

    if list_option == 4:
        print('\nDelete existing mortgage enquiry results')

        input('\nPress any key to delete \n')

    if list_option == 5:
        print('Thank you for looking it')
        quit()
        # input('\nPress any key to Exit \n')
        # exit()
        # sys.exit('Thank you for looking it')

        # input('\nPress any key to Exit \n')

# menu = menu_list()
# print(menu)
