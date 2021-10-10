# -*- coding: utf-8 -*-

from datetime import datetime
import time
from datetime import datetime
from timer_decorator import timing


def modify(func):
    # a decorator that only calls a decorated function during the day

    def wrapper(x, y):
        time.sleep(1)
        now = datetime.now().time() # time object
        print(f'modify_1 x= {x}, y= {y}, {func.__name__}, {now}')
        return func(x, y)

    return wrapper


def modify_2(func):
    # a decorator that only calls a decorated function during the day
    def wrapper(x, y):
        time.sleep(1)
        now = datetime.now().time() # time object
        print(f' modify_2 x= {x}, y= {y}, {func.__name__}, {now}')
        return func(x, y) -100

    return wrapper


def run_only_between(from_=7, to_=22):
    # a decorator that only calls a decorated function at certain times
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()
        return wrapper
    return dec


@timing
# @modify_2
# @modify
def do_something(x, y, *args, **kw):
    output = (x ** 2) + (y ** 2)
    return output


@timing
@modify_2
@modify
def suma(a, b):
    output = (a + b)
    return output

@timing
@run_only_between(7, 10)
def say_something():
    print("Hello world")


if __name__ == '__main__':
    print(do_something(5, 4, 0, kazkoks_kwargas=606, kw_2=0))
    print(suma(5, 4))
    say_something()
