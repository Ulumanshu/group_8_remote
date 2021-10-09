# -*- coding: utf-8 -*-

from datetime import datetime


def disable_at_night(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print('MODIFIKUOTA WRAPERIO')
            func()
            print("PO ORGINALO PALEIDIMO DAR KAZKAS")
    return wrapper


@disable_at_night
def say_something():
    print("Hello world")


say_something()