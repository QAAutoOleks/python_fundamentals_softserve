string_list = ['1', '2', '3', '4', '5', '7']
int_list_1 = []

for i in string_list:
    int_list_1.append(int(i))

int_obj = map(int, string_list)

print(int_list_1)
print(list(int_obj))
