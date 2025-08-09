def valid_number(input_number):
    if not isinstance(input_number, int):
        raise TypeError('Number must be integer')
    elif input_number == 0:
        raise ValueError('Number can\'t be zero')
    
def check_odd_even(input_number):
    if input_number % 2 == 0:    
        'Entered number is even'
    elif input_number %2 != 0:
        'Entered number is odd'
    else:
        'You entered not a number.'
