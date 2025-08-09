class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_positive(number):
    try:
        number = float(number)
        if number > 0:
            return f'You input positive number: {number}'
        else:
            raise MyError(f'You input negative number: {number}. Try again.')
    except MyError as m:
        return m
    except:
        return 'Error type: ValueError!'
    
print(check_positive(-9))