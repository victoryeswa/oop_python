import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 sec...')
    time.sleep(1)
    print('Done sleeping...')

processes = []

for _ in range(10):
    p = multiprocessing.process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')


#addingarguments