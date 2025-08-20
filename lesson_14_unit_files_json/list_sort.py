some_list = [4, -6, 7, 100, 3]

def sort_func(given_list):
    sorted_list = []
    for number in given_list:
        for i, val in enumerate(sorted_list):
            if number < val:
                sorted_list.insert(i, number)
                break
        else:
            sorted_list.append(number)
    return sorted_list


print(sort_func(some_list))