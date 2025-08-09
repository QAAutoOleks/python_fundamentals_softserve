class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)
    
def valid_data(number):
    if not isinstance(number, (float, int)):
        return 'Error type: ValueError!'
    if number > 0:
        return f'You input positive number: {number}'
    elif number < 0:
        raise MyError(f'You input negative number: {number}. Try again.')

def check_positive(number):
    try:
        return valid_data(number)
    except MyError as m:
        return m
    
print(check_positive(8.9))