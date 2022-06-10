""" 
get data from user and 
calculate monthly repayment 
"""

def get_loan_data():
    """ get data from user """

    price = float(input('Please enter property price: '))
    loan_amount = float(input('Please enter loan amount: '))
    loan_term = float(input('Please enter term loan: '))

    return [price, loan_amount, loan_term]
    
def calculate_monthly_repayment(loan_amount, loan_term):
    """ calculate monthly repayment """

    rate_of_interest = 4.5
    interest = (rate_of_interest*loan_amount*loan_term)/100
    total_repayment_amount = interest + loan_amount

    return total_repayment_amount/(loan_term*12)

# get_loan_data()