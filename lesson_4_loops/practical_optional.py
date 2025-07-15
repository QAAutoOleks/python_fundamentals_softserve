list_int = '-2, 7, -13, 5'

list_int = list_int.replace(' ', '')
list_string_splitted = list_int.split(',')
list_int_final = []
for i in list_string_splitted:
    list_int_final.append(int(i))
print(list_int_final)

list_float = []
for j in list_int_final:
    list_float.append(float(j))
print(list_float)
