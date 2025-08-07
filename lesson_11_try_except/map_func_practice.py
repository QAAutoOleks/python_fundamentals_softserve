# some_string = '1, 2,3,4,5'
# converted_list = [int(i.strip()) for i in some_string.split(',')]
# print(converted_list)

some_list = ['1', '2', '3']
map_list = map(int, some_list)
print(list(map_list))