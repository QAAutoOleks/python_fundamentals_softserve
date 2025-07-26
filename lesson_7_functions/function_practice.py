def my_func(first_param = 3, second_param = 1) :
    first_param = first_param + second_param

    second_param += 1
    print(first_param, second_param)
my_func(second_param = 1, first_param = 3)