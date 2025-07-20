quantity_of_numbers = 3
print(f"Enter {quantity_of_numbers} numbers..")
list_of_integers = [int(input(f"Enter {i+1} number: ")) for i in range(quantity_of_numbers)]

print(f"Max value is: {max(list_of_integers)}")
print(f"Min value is: {min(list_of_integers)}")
