def valid_number(input_number):
    if not isinstance(input_number, int):
        raise TypeError('Number must be integer')
    
def check_odd_even(input_number):
    try:
        valid_number(input_number)
        return 'Entered number is even' if input_number % 2 == 0 else 'Entered number is odd'
    except:
        return'You entered not a number.'
