import json

file_cars = open("cars.json", "r")
cars_dict_1 = json.load(file_cars)
file_cars.close()

file_cars2 = open("cars2.json", "r")
cars_dict_2 = json.load(file_cars2)
file_cars2.close()

result_file = open("result.json", "w")

if isinstance(cars_dict_1, dict):
    cars_dict_1 = [cars_dict_1]

if isinstance(cars_dict_2, dict):
    cars_dict_2 = [cars_dict_2]

merged_list = cars_dict_1 + cars_dict_2
sorted_dict = sorted(merged_list, key=lambda speed: speed["max_speed"])
result_file.write(json.dumps(sorted_dict))
result_file.close()