decimal = int(input())

result = ''
while decimal > 0:
    result = str(decimal % 2) + result
    decimal = decimal // 2

print(result if result != '' else 0)