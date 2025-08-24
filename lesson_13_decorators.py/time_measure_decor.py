import time

def measure_func(func_cycle):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        func_cycle(*args, **kwargs)
        end_time = time.perf_counter()

        return end_time - start_time
    
    return inner

@measure_func
def func_cycle(given_range):
    for i in range(given_range):
        time.sleep(1)

print(func_cycle(2))