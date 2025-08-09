def divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError(f'Oops, {numerator}/{denominator}, division by zero is error!!!')
        elif (not isinstance(numerator, (int, float)) or 
              not isinstance(denominator, (int, float))):
            raise TypeError('Value Error! You did not enter a number!')
        else:
            return f'Result is {numerator / denominator}'
    except ZeroDivisionError as z:
        return z
    except TypeError as t:
        return t
    
print(divide(4, 8))
            
            