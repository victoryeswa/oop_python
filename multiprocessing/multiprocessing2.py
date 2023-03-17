import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

finish = time.perf_counter()



print(f'Finished in {round(finish-start,)} second(s)')