import timeit


def count(_from, _to):
    while _from >= _to:
        _from -= 1
        _from /= 100
        _from *= 100


def wo_threading_func():
    count(400000, 0)


def with_threading_func():
    import threading

    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    wo_threading = "wo_threading_func()"
    with_threading = "with_threading_func()"
    setup = "from __main__ import wo_threading_func, with_threading_func"

    print("Without threads:", timeit.timeit(
        stmt=wo_threading,
        setup=setup,
        number=100)
    )
    print("With threads:", timeit.timeit(
        stmt=with_threading,
        setup=setup,
        number=100
    ))