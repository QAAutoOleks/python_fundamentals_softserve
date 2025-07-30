def input_numbers_getting():
    number_1 = int(input("Enter number 1: "))
    number_2 = int(input("Enter number 2: "))
    return [number_1, number_2]

def addition():
    required_numbers = input_numbers_getting()
    return print("The sum of Number 1 and Number 2 is equal: {}"
                 .format(required_numbers[0] + required_numbers[1]))

def subtraction():    
    required_numbers = input_numbers_getting()
    return print("The difference between Number 1 and Number 2 is equal: {}"
                 .format(required_numbers[0] - required_numbers[1]))

def multiplication():
    required_numbers = input_numbers_getting()
    return print("The product of the multiplication Number 1 on Number 2 is equal: {}"
                 .format(required_numbers[0] * required_numbers[1]))

def division():
    required_numbers = input_numbers_getting()
    return print("The quotient of the division Number 1 by Number 2 is equal: {}"
                 .format(required_numbers[0] / required_numbers[1]))

if __name__ == '__main__':
    print("Hello from module 'module_with_functions'!")
else:
    print("Hello from module 'Calculator'!")