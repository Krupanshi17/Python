"""Multiprocessing means:
    Running multiple processes simultaneously to achieve true parallelism.
    Multiprocessing=multiple program running together

    The GIL(global  interpreter lock) ensures that only one thread can execute Python bytecode at a time, even on a multi-core CPU. 
    Because of this, multithreading cannot fully utilize multiple CPU cores for CPU-bound tasks such as heavy 
    calculations or data processing.
    Multithreading is limited by the GIL, so multiprocessing is used to achieve true parallelism for CPU-bound tasks.
    """

import multiprocessing
import time


start= time.perf_counter()

def do_something():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done Sleeping")


processes=[]
for _ in range(5):
    p=multiprocessing.Process(target=do_something)
    processes.append(p)
    p.start()

for process in processes:
    process.join()
finish=time.perf_counter()

print(f"Finished in {finish-start} seconds")



"""Processing with a pool of workers
A pool of worker processes is created, and tasks are distributed among them.
The pool manages the worker processes, handling task assignment and result collection.
This approach is efficient for parallelizing tasks that can be executed independently."""

from multiprocessing import Pool    

def square(n):
    return n*n

if __name__=="__main__":
    with Pool(processes=4) as pool:
        result=pool.map(square,[1,2,3,4,5])

    print(result)

#Sharing data between processes
#Processes do NOT share memory by default.To share data, Python gives special tools.
"""Value-Share a single value between processes.
Array-Share Multiple values between processes.
Manager-Share complex objects like lists and dictionaries between processes.
Queue — Share data between processes safely
"""

from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter=Value('i', 0)  
    lock=Lock()

    processes=[Process(target=increment,args=(counter,lock)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(counter.value)
