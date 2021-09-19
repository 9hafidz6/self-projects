# testing multithreading, synchronization, lock, semaphore and condition (cv)
# https://docs.python.org/3/library/threading.html#

import threading
import os
import sys
import time

sem = threading.Semaphore()

x = 0

def threaded_task(thread_str):
    print(f"{threading.current_thread().getName()}") # returns the name assigned to this current thread, this and below works
    # print(f"{threading.current_thread().name}") 

    # print(threading.current_thread()) # returns the thread name as well as something else, not sure
    
    global x
    for _ in range(10):
        sem.acquire()
        x += 1
        sem.release()

def main():
    global x
    x = 0
    thread1 = "thread 1"
    thread2 = "thread 2"
    # the way to implement thread below will cause a synchronization issue
    # can pass arguments as a tuple (need ',' at the end) or a list
    t1 = threading.Thread(target=threaded_task, args=[thread1], name = 't1')
    t2 = threading.Thread(target=threaded_task, args=(thread2,), name = 't2')

    # this way to implement thread does not seem to have synchronization issues but the name is MainThread so ... above might be better
    # can pass in an argument without the use of 'args = ...' perimeter
    # t1 = threading.Thread(target=threaded_task(thread1), name = 't1')
    # t2 = threading.Thread(target=threaded_task(thread2), name = 't2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main()
        print(f"iteration {i}: x = {x}")
    # main()

