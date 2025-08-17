list_miles = [100, 10, 5]

def miles_converter_kilometers(miles):
    return miles * 1.6

kilometers_obj_1 = map(miles_converter_kilometers, list_miles)
kilometers_obj_2 = map(lambda x: x * 1.6, list_miles)

print('obj_1: {}'.format(list(kilometers_obj_1)))
print('obj_2: {}'.format(list(kilometers_obj_2)))