lst = input()
first_list = [int(i.strip()) for i in lst.split(',')]
result = []

for int_element in first_list:
    if first_list.count(int_element) % 2 != 0 and result.count(int_element) == 0:
        result.append(int_element)

print(result)