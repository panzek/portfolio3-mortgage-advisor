"""
get data from user and
calculate monthly repayment
"""
from print import print_red, print_yellow

euro = chr(8364)


def get_loan_data():
    """ get data from user """

    while True:
        try:
            price = float(input(f'Please enter property price: {euro}'))
            loan_amount = float(input(f'Please enter loan amount: {euro}'))

            loan_value = int((loan_amount/price)*100)
            if loan_value >= 90:
                print_red(
                    'Mortgage amount cannot exceed 90% of purchase price'
                    )
                continue

        except ValueError:
            print_red('Not a number, please try again!')
            continue

        try:
            loan_term = float(input('Please enter term loan: '))

            if loan_term < 5 or loan_term > 35:
                print_red('Number of years must be between 5 and 35')
                continue

        except ValueError:
            print_red('Not a number, please try again!')
            continue

        else:
            monthly_repayment = calculate_monthly_repayment(
                price, loan_amount, loan_term
                )
            loan = [price, loan_amount, loan_term, monthly_repayment]
            return loan


def calculate_monthly_repayment(price, loan_amount, loan_term):
    """ calculate monthly repayment """

    rate_of_interest = 2.90
    interest = (rate_of_interest*loan_amount*loan_term)/100
    total_repayment_amount = interest + loan_amount

    monthly_repayment_amount = total_repayment_amount/(loan_term*12)

    loan_value = int((loan_amount/price)*100)

    print_yellow('RESULTS'.center(25))
    print('=============='.center(25))
    print(f'For a mortgage of: \033[1;36m{euro}{price:,.2f}\033[00m')
    print(
        f'Your monthly repayment would be: \033[1;36m{euro}{monthly_repayment_amount:,.2f}\033[00m'
        )
    print(f'with Loan to value (LTV) of: \033[1;36m{loan_value}%\033[00m')
    print(f'And an interest rate of: \033[1;36m{rate_of_interest}%\033[00m')
    print('=============='.center(25))

    print_red('\nDisclaimer:')
    print('This mortgage calculator is for illustrative')
    print('purposes only and does not constitute approval')
    print('in principle or an offer of loan facilities')

    return monthly_repayment_amount
