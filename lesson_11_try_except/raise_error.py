def get_age(age):
    if age < 0:
        raise ValueError('Only positive integers are allowed')
    
try:
    first_num = int(input("Please enter first number\n"))
    second_num = int(input("Please enter second number\n"))
    result = first_num / second_num
except ZeroDivisionError as z:
    print(f'Error: {z}')
else:
    print(f'First number / second number = {first_num / second_num:.2f}')