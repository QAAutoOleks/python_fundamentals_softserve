import time


def measure_func(base_func):

    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        base_func(*args, **kwargs)
        end_time = time.perf_counter()

        return end_time - start_time
    
    return inner

@measure_func
def cycle_func():
    create_list = []
    for i in range(100000000):
        create_list.append(i)

@measure_func
def map_func():
    create_list = list(map(lambda x: x, range(100000000)))

@measure_func
def compreh_func():
    create_list = [x for x in range(100000000)]

print(cycle_func())
print(map_func())
print(compreh_func())