"""
get data from user and
calculate monthly repayment
"""
euro = chr(8364)


def get_loan_data():
    """ get data from user """

    price = float(input(f'Please enter property price: {euro}'))
    loan_amount = float(input(f'Please enter loan amount: {euro}'))
    loan_term = float(input('Please enter term loan:\n'))
    monthly_repayment = calculate_monthly_repayment(price, loan_amount, loan_term)

    return [price, loan_amount, loan_term, monthly_repayment]


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
    print('results are calculated using the interest rates below.')

    return monthly_repayment_amount
