def compreh_list(input):
    return [int(i.strip()) for i in input.split(',')]
    
def map_list(input):
    return list(map(lambda x: int(x.strip()), input.split(',')))

def enum_compreh(given_input):
    result = []
    for j, a in enumerate(compreh_list(given_input)):
        result.append(j + a)

    return result

def enum_map(given_input):
    result = []
    for j, a in enumerate(map_list(given_input)):
        result.append(j + a)

    return result

print(enum_compreh('1,  2, 3,  4'))
print(enum_map('1, 2,  3,  4'))