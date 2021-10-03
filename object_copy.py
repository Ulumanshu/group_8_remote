# -*- coding: utf-8 -*-

from copy import deepcopy

from dataclasses import dataclass
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


# Naujas budas klasesms @dataclass

class Rectangle(Figure):
    __count = 0

    def __init__(self, a, b):
        # self._pi = 1
        self.a = a
        self.b = b
        self._id = self._count()

    def __new__(cls, *args, **kwargs):
        instance = super(Rectangle, cls).__new__(cls)
        print(args, kwargs)
        if args:
            instance.__init__(args[0], args[1])
        else:
            # instance.__init__(args[0], args[1])
            print("No args")
        return super(Rectangle, cls).__new__(cls)

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)

        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)

        return result

    # def __repr__(self) -> str:
    #     return f"Rectangle-id: { self._id }, (a={self.a}, b={self.b})"

    @classmethod
    def _count(cls):
        cls.__count += 1
        return cls.__count

    @property
    def id(self):
        return self._id

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == "__main__":
    p1 = Rectangle(3, 4)
    lst = [1, p1, 3]
    shallow_copy_lst = list(lst)  # lst.copy()
    deep_copy_lst = deepcopy(lst)
    lst[1].a = 5  # we change the value of the side of the rectangle
    print(lst, shallow_copy_lst, deep_copy_lst)
    listu_listas = [lst, shallow_copy_lst, deep_copy_lst]
    for list_ in listu_listas:
        for i in list_:
            if isinstance(i, Rectangle):
                print(i.id, i.a, i.b)
            else:
                print(i)
