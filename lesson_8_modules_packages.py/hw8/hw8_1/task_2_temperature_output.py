import task_2_temperature_module as module

module.FREEZING_POINT = 0
module.BOILING_POINT = 100

users_input = float(input())

module.print_water_state(users_input)