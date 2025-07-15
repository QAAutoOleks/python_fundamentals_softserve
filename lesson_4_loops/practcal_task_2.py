decimal = int(input())

result = ''
while decimal: # if decimal == 0: False
    result = str(decimal % 2) + result
    decimal = decimal // 2

print(result if result != '' else 0)