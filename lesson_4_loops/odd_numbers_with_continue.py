list_with_odd_numbers = []
for i in range(100):
    if i % 2 == 0:
        continue
    list_with_odd_numbers.append(i)
else:
    print(list_with_odd_numbers)