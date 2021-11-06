import threading
import time

abc = [1, 2]


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_cube(num):
    # A function that returns the third power of a number given as a parameter
    time.sleep(5)
    print(f"Cube: {num * num * num}")


def print_square(num):
    # A function that returns the square of the number given as a parameter
    time.sleep(5)
    return num * num


def iterate_print(iter):
    # A function prints the elements of a list
    for item in iter:
        print(item)


if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=iterate_print, args=(range(100),))  # writing out successive natural numbers
    t2 = threading.Thread(target=iterate_print, args=("Python"*1000,))  # writing the characters of the string

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    t1.join()
    print("T1 DONE")
    t2.join()

    print("Done!")
    # creating  threads
    t1 = ThreadWithReturnValue(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    print(t1.join())
    t2.join()

    print("Done!")