"""
get data from user and
calculate monthly repayment
"""
euro = chr(8364)


def get_loan_data():
    """ get data from user """

    price = float(input(f'Please enter property price: {euro}'))
    loan_amount = float(input(f'Please enter loan amount: {euro}'))
    loan_term = float(input('Please enter term loan: '))
    monthly_repayment = calculate_monthly_repayment(loan_amount, loan_term)

    return [price, loan_amount, loan_term, monthly_repayment]


def calculate_monthly_repayment(loan_amount, loan_term):
    """ calculate monthly repayment """

    rate_of_interest = 10
    interest = (rate_of_interest*loan_amount*loan_term)/100
    total_repayment_amount = interest + loan_amount

    monthly_repayment_amount = total_repayment_amount/(loan_term*12)

    print(
        f'{chr(10)}Mortgage repayment: {euro}{monthly_repayment_amount:.2f}'
        )
    print('Loan to value (LTV): 66.8%')
    print('Total interest at 2.6%')

    return monthly_repayment_amount
