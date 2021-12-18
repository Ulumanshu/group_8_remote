class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print('INSTANCES', cls._instances, type(cls._instances))
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonType):
    pass

class SingletonClass(object):   # NB must be subclass of object to use __new__
    instance = None             # Singleton naudojamas, kad programoje vienas instance (pasirinktas) būtų naudojamas tik vieną kartą

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is not None:
            raise Exception('Singleton Instance Already exists!')
        cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self):
        pass
        # initialisation code...

    @classmethod
    def get_instance(cls):
        if cls.instance is not None:
            return cls.instance
        return cls()


x = SingletonClass()
y = SingletonClass()
z = SingletonClass()

abc = [x, y, z]

print(abc)
print(x == y)

