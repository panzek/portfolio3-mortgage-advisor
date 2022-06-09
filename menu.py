""" Options menu """

def menu_list():
    """ List of options """

    while True:
        print('\nPlease choose one of the following options:')
        print('\n1. To run an overview of the application')
        print('2. To run through the instructions')
        print('3. To run new enquiry')
        print('4. To delete all existing enquiry results')
        print('9. To exit the application\n')

        int(input('Please enter your option: 1,2,3,4, or 9: \n'))
        