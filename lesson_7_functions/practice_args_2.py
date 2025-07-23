def print_sum_of_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    print(f"Sum of given numbers = {sum}")

print_sum_of_numbers(1, 2, 3, 4, 5)