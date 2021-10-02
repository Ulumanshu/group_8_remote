# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from math import pi


# Paprasta klase
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def show_finance(self):
        return 0


# Simple inheritance
# Paprastas pavedejimas (1na tevine klase)
class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        # Specify what super class to use if using multiple inheritance
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


# Simple inheritance
# Paprastas pavedejimas (1na tevine klase)
class Student(Person):
    def __init__(self, name, age, scholarship):
        # Specify what super class to use if using multiple inheritance
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


# Multiple inheritance
# Daugybinis paveldejimas (paveldi daugiau nei viena klase)
class WorkingStudent(Student, Employee):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        # Specify what super class to use if using multiple inheritance
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


# Abstract class example
# Abstrakcios klases pavyzdys - naudojama kaip sablonas kitoms klases, @abstractmethod privercia kitus programuotojus
# kuriant klases kurios paveldi Figure aprasyti area ir circuit metodus
class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


# Class inheriting from Figure has to have circuit and area methods defined
# Klase paveldinti is Figure turi tureti apibreztus metodus circuit ir area
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def circuit(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2


if __name__ == "__main__":
    ##################### INHERITANVE/PAVELDEJIMAS #####################################################################
    os1 = Person("John", 54)
    os2 = Employee("Jack", 36, 20, 160)
    os3 = Student("Agatha", 22, 1000)
    os4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
    object_list = [os1, os2, os3, os4]
    # Polymorphism, using show_finance methods on object list made of objects with different classes. All classes have
    # show_finance method implemented
    # Polimorfizmas, naudojamas show_finance metodas objektu sarasui, sarase objektai sukurti is skirtingu klasiu,
    # polimorfizmas ir yra tai, visos tos klases turi metoda tuo pat pavadinimu.
    # for i in object_list:
    #     print(f'{i} finasai: {i.show_finance()}')

    # print(os1)
    # print(os2)
    # print(os3)
    # print(os4)
    ####################################################################################################################
    ############### ABSTRACT CLASSES / ABSTRAKCIOS KLASES ##############################################################
    Rectangle = Rectangle(3, 5)
    Circle = Circle(12)
    print(Rectangle.circuit())
    print(Circle.circuit())
