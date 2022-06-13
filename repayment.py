"""
get data from user and
calculate monthly repayment
"""
euro = chr(8364)


def get_loan_data():
    """ get data from user """
    while True:
        try:
            price = float(input(f'Please enter property price: {euro}'))
            loan_amount = float(input(f'Please enter loan amount: {euro}'))
            loan_term = float(input('Please enter term loan:'))
            monthly_repayment = calculate_monthly_repayment(price, loan_amount, loan_term)
            loan =  [price, loan_amount, loan_term, monthly_repayment]

            if isinstance(loan, str):
                raise ValueError('must enter a username')

        except ValueError as error_msg:
            print(f'{error_msg} is not a number')

        else:
            return loan

    # return [price, loan_amount, loan_term, monthly_repayment]

def get_loan(price):
    """ get data from user """

    while True:
        try:
            price = float(input(f'Please enter property price: {euro}')) 
            print(f'{price} not a number')
        except ValueError:
            print(' is not a number')

def calculate_monthly_repayment(price, loan_amount, loan_term):
    """ calculate monthly repayment """

    rate_of_interest = 10
    interest = (rate_of_interest*loan_amount*loan_term)/100
    total_repayment_amount = interest + loan_amount

    monthly_repayment_amount = total_repayment_amount/(loan_term*12)

    print('RESULTS'.center(25)) 
    print('=============='.center(25))
    print(f'{chr(10)}For a mortgage of: {euro}{price}')
    print(
        f'Your monthly repayment would be: {euro}{monthly_repayment_amount:.2f}'
        )
    print('with Loan to value (LTV) of: 66.8%')
    print(f'An interest rate of: {rate_of_interest}')
    print('=============='.center(25))

    print('\nThe above mortgage calculator results are estimates') 
    print('based upon the information you have provided. The') 
    print('results are calculated using a fixed interest rate.')

    return monthly_repayment_amount
