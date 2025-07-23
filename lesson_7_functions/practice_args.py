def print_numbers(number, *args):
    print("argument: ")
    print(number)
    print("vartuple: ")
    for var in args:
        print(var)

print_numbers(10)
print("-" * 10)
print_numbers(70, 60, 50, 40)