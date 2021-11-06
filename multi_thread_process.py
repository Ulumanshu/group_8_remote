import threading


abc = [1, 2]

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