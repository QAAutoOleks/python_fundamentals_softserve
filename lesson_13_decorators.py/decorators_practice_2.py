def smart_printing(func):
    print('This function decorates text')

    def inner(text):
        if text == 'tomato':
            print('# ', end='')
            func(text)
            print(' #')
        elif text == 'salad':
            print('~ ', end='')
            func(text)
            print(' ~')

    return inner

@smart_printing
def printer(text):
    print(text, end='')

printer('salad')
printer('tomato')