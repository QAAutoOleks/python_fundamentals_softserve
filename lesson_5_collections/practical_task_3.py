lst = input()
list_of_all_elements = [i.strip() for i in lst.split(',')]
result = []

for element in list_of_all_elements:
    if element.isdigit():
        result.append(int(element))

print(result)