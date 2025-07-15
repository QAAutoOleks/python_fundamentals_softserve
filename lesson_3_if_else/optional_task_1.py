number = input()

if number[0] == "-" and number[1:].isdecimal():
    result = len(number) - 1
elif number.isdecimal():
    result = len(number)
else:
    result = "Wrong data type"

print(result)