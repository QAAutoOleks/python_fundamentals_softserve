import module_with_functions

def main():
    print("Choose operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

main()
chosen_option = int(input())
number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))

match chosen_option:
    case 1:
        module_with_functions.addition(number_1, number_2)