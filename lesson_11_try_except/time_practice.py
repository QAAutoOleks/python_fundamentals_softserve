try:
    a = int(input("Enter int value "))
    a % 2 == 0
    print("Number is even")
except ValueError:
    print("Wrong input!")