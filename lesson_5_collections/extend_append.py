list_1 = [1, 2]
list_2 = [3, 4]
set_1 = {1, 2}
tuple_1 = (3, 4)

list_1.append(list_2)
print(list_1)
list_1.extend(list_2)
print(list_1)
# list_set = list.extend(set_1) - Error
list_1.extend(tuple_1)
print(list_1)