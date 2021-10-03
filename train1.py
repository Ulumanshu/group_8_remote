# -*- coding: utf-8 -*-
class Person:

    def __init__(self, name, age, atlyginimas, stazas):
        self.name = name
        self.age = age
        self.atlyginimas = atlyginimas
        self.stazas = stazas

    def __str__(self):
        return f"{self.name} is {self.age} years old."
#    @staticmethod   # prieina prie visko: ir prie __init__ metode aprasytu kintamuju ir "kietu" kintamuju
    @classmethod    # uzblokuoja priejima prie konstruktoriaus __init__ metode aprasytu kintamuju == objekto kintamuju tampa cls
    def show_finance(self, atlyginimas, stazas):
        return atlyginimas * stazas

if __name__ == "__main__":
    p1 = Person('Petras', 25, 1000, 36)
    print(p1.show_finance(p1.atlyginimas, p1.stazas))
    print(Person.show_finance(900, 24))