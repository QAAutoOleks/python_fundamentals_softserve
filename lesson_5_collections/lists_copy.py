first_list = ['1', '2', '3']

second_list = first_list.copy()
print(second_list)

third_list = list(first_list)
print(third_list)

print('0'.join(first_list)) #output: 10203

some_set = {1, 2, 3}
some_set.discard(3)
print(some_set)
set_2 = set()

# set_2 = some_set.copy()
#set_2 = set(some_set)
# set_2.update(some_set)
# set_2 = some_set
# print(set_2)


dict_1 = {"age":11, "name":"Ivan"}
dict_2 = {"name":"Ivan", "age":11}
print(dict_1 == dict_2)

list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))