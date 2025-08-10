def bigger_zero_and_is_integer(number):
    return(number > 0, isinstance(number, int))

def check_age(age):
    match bigger_zero_and_is_integer(age):
        case (True, True):
            print(age)
        case _:
            raise ValueError

while True:
    try:
        age = int(input())
        check_age(age)
        break
    except (ValueError, TypeError):
        pass