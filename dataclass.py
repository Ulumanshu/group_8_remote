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


# Naujas budas klasesms @dataclass
@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

# Senu budu butu tiek:
# class Rectangle(Figure):
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __repr__(self) -> str:
#         return f"Rectangle(a={self.a}, b={self.b})"
#
#     def __eq__(self, other) -> bool:
#         return isinstance(other, Rectangle) and (self.a, self.b) == (other.a, other.b)
#
#     def circuit(self) -> float:
#         return 2 * (self.a + self.b)
#
#     def area(self) -> float:
#         return self.a * self.b


if __name__ == "__main__":
    rect1 = Rectangle(1, 2)
    print(rect1.area(), rect1.circuit())
    p1 = Rectangle(3, 4)
    p2 = Rectangle(3, 4)
    print(p1)
    print(p1 == p2)
