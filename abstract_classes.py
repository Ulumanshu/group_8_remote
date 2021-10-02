# -*- coding: utf-8 -*-

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


if __name__ == "__main__":
    os1 = Person("John", 54)
    os2 = Employee("Jack", 36, 20, 160)
    os3 = Student("Agatha", 22, 1000)
    os4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
    object_list = [os1, os2, os3, os4]
    # Polymorphism, using show_finance methods on object list made of objects with different classes. All classes have
    # show_finance method implemented
    # Polimorfizmas, naudojamas show_finance metodas objektu sarasui, sarase objektai sukurti is skirtingu klasiu,
    # polimorfizmas ir yra tai, visos tos klases turi metoda tuo pat pavadinimu.
    for i in object_list:
        print(f'{i} finasai: {i.show_finance()}')

    # print(os1)
    # print(os2)
    # print(os3)
    # print(os4)
