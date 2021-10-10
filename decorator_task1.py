# -*- coding: utf-8 -*-

from datetime import datetime
import time

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

if __name__ == '__main__':
    print(do_something(5, 4))
    print(suma(5, 4))