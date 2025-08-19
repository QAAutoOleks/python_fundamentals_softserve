import json
file_cars = open("cars.json", "r")
cars_dict_1 = json.load(file_cars)
collect_array = [car['max_speed'] for car in cars_dict_1]
file_cars2 = open("cars2.json", "r")
cars_dict_2 = json.load(file_cars2)
collect_array.append(cars_dict_2[0]['max_speed'])
collect_array = sorted(collect_array)
result_file = open("result.json", "w")
result_file.write(collect_array)