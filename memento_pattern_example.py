import pickle


class SimpleClass:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f"SimpleClass('{self.name}', {self.count})"


sc1 = SimpleClass('test', 10)
repr = repr(sc1)
sc2 = eval(repr)
print("ATKURAT IS REPR: ", sc2)


class NotSoSimpleClass:
    def __init__(self, name='', count=0):
        self.name = name
        self.count = count

    def get_state(self):
        return pickle.dumps(self.__dict__)

    def restore_state(self, memento):
        self.__dict__.clear()
        self.__dict__.update(pickle.loads(memento))


sc1 = NotSoSimpleClass('test', 10)
memento = sc1.get_state()
sc22 = NotSoSimpleClass()
sc22.restore_state(memento)

print(sc22)