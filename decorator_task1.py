# -*- coding: utf-8 -*-

from datetime import datetime


def modify(func):
    # a decorator that only calls a decorated function during the day
    def wrapper(x, y):
        return func(x, y)

    return wrapper


@modify
def do_something(x, y):
    output = (x ** 2) + (y ** 2)
    return output


print(do_something(5, 4))
