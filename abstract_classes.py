# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


if __name__ == "__main__":
    os1 = Person("John", 54)
    os2 = Employee("Jack", 36, 20, 160)
    os3 = Student("Agatha", 22, 1000)
    print(os1)
    print(os2)
    print(os3)
