import module_with_functions as calc_module

def main():
    print("Choose operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

main()
chosen_option = int(input())

match chosen_option:
    case 1:
        calc_module.addition()
    case 2:
        calc_module.subtraction()
    case 3:
        calc_module.multiplication()
    case 4:
        calc_module.division()
    case _:
        print("Input ERROR")