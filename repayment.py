""" calculate repayment """

def first_time_buyer(price,amount,term):
    """username function to get data from user"""

    while True:
        interest = (price*amount*term)/100
        print(interest)

        price = float(input('Please enter property price: '))
        amount = float(input('Please enter loan amount: '))
        term = float(input('Please enter term loan: '))

    return interest

first_time_buyer()