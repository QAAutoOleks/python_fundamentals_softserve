def smart_dividing(func):
    print('This function performs smart dividing')

    def inner(a, b):
        if b == 0:
            print('ZeroDivisionError')
            return None
        return func(a, b)
    
    return inner

@smart_dividing
def dividing(a, b):
    return a / b
