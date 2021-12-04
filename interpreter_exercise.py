from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from string import digits


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request, variables) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any, variables) -> AbstractExpression:
        if self._next_handler:
            return self._next_handler.handle(request, variables)

        return None


class AdditionHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        if request == "+":
            return Add(Number(variables[0]), Number(variables[1]))
        else:
            return super(AdditionHandler, self).handle(request, variables)


class SubtractionHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        if request == "-":
            return Subtract(Number(variables[0]), Number(variables[1]))
        else:
            return super(SubtractionHandler, self).handle(request, variables)


class AbstractExpression:
    "All Terminal and Non-Terminal expressions will implement an `interpret` method"
    @staticmethod
    def interpret():
        """
        The `interpret` method gets called recursively for each
        AbstractExpression
        """


class Number(AbstractExpression):
    "Terminal Expression"

    def __init__(self, value):
        if isinstance(value, str):
            self.value = int(value)
        if isinstance(value, AbstractExpression):
            self.value = value.interpret()

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Add(AbstractExpression):
    "Non-Terminal Expression."

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        print('LR', self.left, self.right)
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"


class Subtract(AbstractExpression):
    "Non-Terminal Expression"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"


def client_code(handler: Handler, tokens: list[str]) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """
    operators = [n for n in tokens if n in ["+", "-"]]
    numbers = [p for p in tokens if p in digits]
    print(operators)
    print(numbers)

    for element in operators:
        print(element)
        variables = [numbers[0], numbers[1]]
        result = handler.handle(element, variables)
        numbers.pop(0)
        numbers.pop(0)
        numbers.insert(0, result)
        print(result, type(result), numbers)

    final = numbers.pop(0)
    print(final)
    return final


# The Client
# The sentence complies with a simple grammar of
# Number -> Operator -> Number -> etc,
SENTENCE = "5 + 4 - 3 + 7 - 2"


if __name__ == "__main__":
    TOKENS = SENTENCE.split(" ")

    addhandler = AdditionHandler()
    subtracthandler = SubtractionHandler()

    addhandler.set_next(subtracthandler)

    AST_ROOT = client_code(addhandler, TOKENS)

    print(AST_ROOT)

    # Print out a representation of the AST_ROOT
    print(AST_ROOT.interpret())
