def enum_map(func):
    def wrapper(given_str):      
        created_list = func(given_str)

        result = []
        for j, a in enumerate(created_list):
            result.append(j + a)

        return result    

    return wrapper

@enum_map
def compreh_list(input):
    return [int(i.strip()) for i in input.split(',')]
    
@enum_map
def map_list(input):
    return list(map(lambda x: int(x.strip()), input.split(',')))

print(compreh_list('1,   2, 3'))
print(map_list('1,   2, 3'))