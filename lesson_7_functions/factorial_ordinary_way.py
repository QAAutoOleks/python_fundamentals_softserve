given_number = int(input("Enter real integer number: "))

factorial_output = 1

match given_number:
    case 0, 1:
        print("Factorial of {} = ".format(given_number), factorial_output)
    case a if given_number < 0:
        print("Factorial of negative number doesn't exist")
    case _:
        for i in range(1, given_number+1, 1):
            factorial_output *= i
        print("Factorial of '{}' =".format(given_number), factorial_output)
        