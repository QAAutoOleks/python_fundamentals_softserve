some_input = int(input('Enter an "int" value: '))
match some_input:
    case 0:
        print('Input = 0')
    case 1:
        print('Input = 1')
    case _:
        print('Other...')
        