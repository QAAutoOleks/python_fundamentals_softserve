some_input = ['Text', 1, 2]

match some_input:
    # case 'Tex', 1, 2: - Error
    # case 'Text', *num: - Ok
    # case 'Text', 1, 2: - Ok
    case text, 1, 2: # Ok
        print('Ok')
    case _:
        print('Error')