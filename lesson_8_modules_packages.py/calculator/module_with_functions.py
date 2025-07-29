def input_numbers_getting():
    number_1 = int(input("Enter number 1: "))
    number_2 = int(input("Enter number 2: "))
    return [number_1, number_2]

def addition():
    return print("The sum of Number 1 and Number 2 is equal: {}"
                 .format(input_numbers_getting()[0] + input_numbers_getting()[1]))

def subtraction():    
    return print("The difference between Number 1 and Number 2 is equal: {}"
                 .format(input_numbers_getting()[0] - input_numbers_getting()[1]))

def multiplication():
    return print("The product of the multiplication Number 1 on Number 2 is equal: {}"
                 .format(input_numbers_getting()[0] * input_numbers_getting()[1]))

def division():
    return print("The quotient of the division Number 1 by Number 2 is equal: {}"
                 .format(input_numbers_getting()[0] / input_numbers_getting()[1]))