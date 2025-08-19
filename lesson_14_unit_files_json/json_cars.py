import json

def sort_cars(dict):
    print('Before sorting:', dict)
    sorted = True
    i = 0
    while sorted:
        sorted = False
        try:
            if dict[i]['max_speed'] > dict[i+1]['max_speed']:
                dict[i], dict[i+1] = dict[i+1], dict[i]
                sorted = True
        except:
            i = 0
        i += 1
    return dict

file_cars = open("cars.json", "r")
cars_dict_1 = json.load(file_cars)

print('After sorting', sort_cars(cars_dict_1))

# collect_array = [car['max_speed'] for car in cars_dict_1]
# file_cars2 = open("cars2.json", "r")
# cars_dict_2 = json.load(file_cars2)
# collect_array.append(cars_dict_2[0]['max_speed'])
# collect_array = sorted(collect_array)
# result_file = open("result.json", "w")
# result_file.write(collect_array)