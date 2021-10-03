# -*- coding: utf-8 -*-

from dataclasses import dataclass
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == "__main__":
    rect1 = Rectangle(1, 2)
    print(rect1.area(), rect1.circuit())