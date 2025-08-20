some_list = [4, -6, 7, 100, 3]

def sort_func(given_list):
    iteration = 0
    sorted_list = []
    for number in given_list:
        if not sorted_list:
            sorted_list.append(number)
        elif number < sorted_list[iteration-1]:
            sorted_list.append(number)
            (
            sorted_list[iteration-1], 
            sorted_list[iteration]
            ) = (
            sorted_list[iteration], 
            sorted_list[iteration-1]
            )
        else:
            sorted_list.append(number)

        iteration += 1
    
    return sorted_list

print(sort_func(some_list))