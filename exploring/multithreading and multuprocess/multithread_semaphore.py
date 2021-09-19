# testing multithreading, synchronization, lock, semaphore and condition (cv)
# https://docs.python.org/3/library/threading.html#
# https://stackoverflow.com/questions/2332765/what-is-the-difference-between-lock-mutex-and-semaphore/45567101#45567101

import threading
import os
import sys
import time

# number of semaphore that are available for the threads to run
# if only 1 semaphore, the threads have to take turns 
sem = threading.Semaphore(2)

# can also use mutex or lockm but it is unique. if want many, need different names 
# mutex = threading.Lock() # equal to threading.Semaphore(1)


def threaded_task1(thread_str):   
    x = 0
    for _ in range(10):
        sem.acquire()
        x += 1
        sem.release()
        print(f"{threading.current_thread().getName()} : {x}")
        time.sleep(0.1)


def threaded_task2(thread_str):    
    x = 0
    for _ in range(10):
        sem.acquire()
        x += 1
        sem.release()
        print(f"{threading.current_thread().getName()} : {x}")
        time.sleep(0.1)

def main():
    global x
    x = 0
    thread1 = "thread 1"
    thread2 = "thread 2"
    # the way to implement thread below will cause a synchronization issue
    # can pass arguments as a tuple (need ',' at the end) or a list
    t1 = threading.Thread(target=threaded_task1, args=[thread1], name = 't1')
    t2 = threading.Thread(target=threaded_task2, args=(thread2,), name = 't2')

    # this way to implement thread does not seem to have synchronization issues but the name is MainThread so ... above might be better
    # can pass in an argument without the use of 'args = ...' perimeter
    # t1 = threading.Thread(target=threaded_task(thread1), name = 't1')
    # t2 = threading.Thread(target=threaded_task(thread2), name = 't2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

