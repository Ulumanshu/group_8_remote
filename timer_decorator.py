from functools import wraps  # Koks tikslas naudoti functools wraps
from time import time


def timing(f):

    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        print("ARGSAI TIMITE: ", args, *args)
        print('KWARGSAI', kw)
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return wrap


@timing
def time_consuming_function():
    sum = 0
    for e in range(700000):
        if e % 2 == 0:
            sum += e

    return sum


if __name__ == '__main__':
    print(time_consuming_function())
