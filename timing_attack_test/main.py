from time import sleep, perf_counter
from statistics import median
from myfuncs import send_post, test_func, send_get

import threading

start_time = perf_counter()

i=0
thread_number = 1000
threads = []

while i < thread_number:
    print(f"thread #{i}")
    i += 1
    x = threading.Thread(target=send_get, args=(1, i))
    threads.append(x)
    x.start()


# print(f"threads: {len(threads)}")

end_time = perf_counter()
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

