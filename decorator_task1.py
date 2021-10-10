# -*- coding: utf-8 -*-

from datetime import datetime
import time
from datetime import datetime


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
    time.sleep(1)
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


@modify_2
@modify
def do_something(x, y):
    output = (x ** 2) + (y ** 2)
    return output


@modify_2
@modify
def suma(a, b):
    output = (a + b)
    return output


@run_only_between(7, 10)
def say_something():
    print("Hello world")


if __name__ == '__main__':
    print(do_something(5, 4))
    print(suma(5, 4))
    say_something()