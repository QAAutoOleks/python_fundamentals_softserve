import json

def sort_cars(dict):
    print('Before sorting:', dict)
    for i in range(1, len(dict)):
        if dict[i]['max_speed'] < dict[i-1]['max_speed']:
            dict[i], dict[i-1] = dict[i-1], dict[i]
    return dict

file_cars = open("cars.json", "r")
cars_dict_1 = json.load(file_cars)

print(sort_cars(cars_dict_1))

# collect_array = [car['max_speed'] for car in cars_dict_1]
# file_cars2 = open("cars2.json", "r")
# cars_dict_2 = json.load(file_cars2)
# collect_array.append(cars_dict_2[0]['max_speed'])
# collect_array = sorted(collect_array)
# result_file = open("result.json", "w")
# result_file.write(collect_array)