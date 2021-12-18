"""A race condition occurs when two or more threads can access shared data
and they try to change it at the same time.
As a result, the values of variables may be unpredictable and vary
depending on the timings of context switches of the processes.
Explanation link: https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
"""
import threading

# global variable x
x = 0


def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1


def thread_task(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(1000000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    # setting global variable x as 0
    x = 0
    lock = threading.Lock()
    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print(f"Iteration {i}: x = {x}")
