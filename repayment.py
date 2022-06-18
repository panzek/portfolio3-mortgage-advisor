"""
get data from user and
calculate monthly repayment
"""
from print import print_red, print_green

euro = chr(8364)


def get_loan_data():
    """ get data from user """

    while True:
        try:
            price = float(input(f'Please enter property price: {euro}'))
            loan_amount = float(input(f'Please enter loan amount: {euro}'))

            loan_value = int((loan_amount/price)*100)
            if loan_value >= 90:
                print_red('Mortgage amount cannot exceed 90% of purchase price')
                continue

        except OverflowError:
            return False

        try:
            loan_term = float(input('Please enter term loan: '))
    
            if loan_term < 5 or loan_term > 35:
                print_red('Number of years must be between 5 and 35')
                continue

        except ValueError:
            return False
        
        try:
            monthly_repayment = calculate_monthly_repayment(price, loan_amount, loan_term)
            loan =  [price, loan_amount, loan_term, monthly_repayment]

            if isinstance(loan, str):
                raise ValueError(loan)

        except ValueError as error_msg:
            print(f'{error_msg} not a number, please try again!')  
            return False      

        else:
            return loan


def calculate_monthly_repayment(price, loan_amount, loan_term):
    """ calculate monthly repayment """

    rate_of_interest = 2.90
    interest = (rate_of_interest*loan_amount*loan_term)/100
    total_repayment_amount = interest + loan_amount

    monthly_repayment_amount = total_repayment_amount/(loan_term*12)

    loan_value = int((loan_amount/price)*100)

    print_green('RESULTS'.center(25))
    print('=============='.center(25))
    print(f'For a mortgage of: {euro}{price:,.2f}')
    print(
        f'Your monthly repayment would be: {euro}{monthly_repayment_amount:,.2f}'
        )
    print(f'with Loan to value (LTV) of: {loan_value}%')
    print(f'And an interest rate of: {rate_of_interest}%')
    print('=============='.center(25))

    print_red('\nDisclaimer:')
    print('This mortgage calculator is for illustrative')
    print('purposes only and does not constitute approval')
    print('in principle or an offer of loan facilities')
    
    return monthly_repayment_amount

