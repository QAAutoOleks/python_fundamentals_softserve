import json

file_cars = open("cars.json", "r")
cars_dict_1 = json.load(file_cars)

file_cars2 = open("cars2.json", "r")
cars_dict_2 = json.load(file_cars2)

result_file = open("result.json", "w")

merged_list = cars_dict_1 + cars_dict_2
sorted_dict = sorted(merged_list, key=lambda speed: speed["max_speed"])
result_file.write(str(sorted_dict))