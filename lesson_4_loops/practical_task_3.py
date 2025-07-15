binary_number = input()

final_list = []
for i in binary_number:
    if i == '1':
        final_list.append(True)
    else:
        final_list.append(False)

print(final_list)