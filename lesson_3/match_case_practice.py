some_input = ['Text', 1, 2]

match some_input:
    # case 'Tex', 1, 2:
    case 'Text', *num:
    # case 'Text', 1, 2:
        print('Ok')
    case _:
        print('Error')