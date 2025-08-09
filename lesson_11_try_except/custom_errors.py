class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)
    
def valid_number(input_number):
    if not isinstance(input_number, int):
        raise CustomError('Number must be integer')
    elif input_number == 0:
        raise CustomError('Number can\'t be zero')
        
user_input = int(input('Enter data: '))

try:
    valid_number(user_input)
    print('Your number is: {}'.format(user_input))
except CustomError as c:
    print('We obtain error: {}'.format(c))