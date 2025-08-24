import time

def some_func(given_range):
    for i in range(given_range):
        time.sleep(1)

start_time = time.perf_counter()
print('Start time:', start_time)
some_func(5)
finish_time = time.perf_counter()
print('Finish time:', finish_time)

elapsed_time = finish_time - start_time
print('Elapsed time:', elapsed_time)