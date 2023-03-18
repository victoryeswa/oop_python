import concurrent.futures
import time


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs =[5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs ]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
