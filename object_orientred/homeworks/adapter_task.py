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

        return handler

    @abstractmethod
    def handle(self, request: Any, variables) -> AbstractExpression:
        if self._next_handler:
            return self._next_handler.handle(request, variables)

        # return None


class AdditionHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        var1 = Number(variables[0])
        var2 = NumberOTHER(variables[1])
        if request == "+":
            return Add(var1, var2)
        else:
            return super(AdditionHandler, self).handle(request, variables)


class SubtractionHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        var1 = Number(variables[0])
        var2 = NumberOTHER(variables[1])
        if request == "-":
            return Subtract(var1, var2)
        else:
            return super(SubtractionHandler, self).handle(request, variables)


class MultiplicationHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        var1 = Number(variables[0])
        var2 = NumberOTHER(variables[1])
        if request == "*":
            return Multiply(var1, var2)
        else:
            return super(MultiplicationHandler, self).handle(request, variables)


class DivisionHandler(AbstractHandler):
    def handle(self, request: Any, variables) -> AbstractExpression:
        var1 = Number(variables[0])
        var2 = NumberOTHER(variables[1])
        if request == "/":
            return Divide(var1, var2)
        else:
            return super(DivisionHandler, self).handle(request, variables)


class AbstractExpressionOTHER:
    "All Terminal and Non-Terminal expressions will implement an `interpret` method"
    @staticmethod
    def interpret_different_interface():
        """
        The `interpret` method gets called recursively for each
        AbstractExpression
        """


class NumberOTHER(AbstractExpressionOTHER):
    "Terminal Expression"

    def __init__(self, value):
        if isinstance(value, str):
            self.value = float(value)
        if isinstance(value, AbstractExpression):
            self.value = value

    def interpret_different_interface(self):
        res = False
        if isinstance(self.value, float):
            res = self.value
        if isinstance(self.value, AbstractExpression):
            res = self.value.interpret()

        return res

    def __repr__(self):
        return str(self.value)


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
            self.value = float(value)
        if isinstance(value, AbstractExpression):
            self.value = value

    def interpret(self):
        res = False
        if isinstance(self.value, float):
            res = self.value
        if isinstance(self.value, AbstractExpression):
            res = self.value.interpret()

        return res

    def __repr__(self):
        return str(self.value)


class Add(AbstractExpression):
    "Non-Terminal Expression."

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
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


class Multiply(AbstractExpression, AbstractExpressionOTHER):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

    def __repr__(self):
        return f"({self.left} Multiply {self.right})"


class Divide(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        if self.right.interpret() > 0:
            res = self.left.interpret() / self.right.interpret()
        else:
            res = 0
        print(self.left, self.right, res)
        print(self.right.interpret() > 0)
        return res

    def __repr__(self):
        return f"({self.left} Divide {self.right})"


def extract_number(text_):
    result = ""
    for char in text_:
        if char in digits:
            result += char
        elif char in [".", ","]:
            result += "."
        else:
            continue
    # print(text_, result)
    return result


def client_code(handler: Handler, tokens: list[str]) -> AbstractExpression:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    operators = [n for n in tokens if n in ["+", "-", "*", "/"]]
    numbers = [extract_number(p) for p in tokens if p not in operators]
    print(operators)
    print(numbers)

    for element in operators:
        variables = [numbers[0], numbers[1]]
        result = handler.handle(element, variables)
        numbers.pop(0)
        numbers.pop(0)
        numbers.insert(0, result)

    final = numbers.pop(0)

    return final


if __name__ == "__main__":
    # The Client
    # The sentence complies with a simple grammar of
    # Number -> Operator -> Number -> etc,

    SENTENCE = "5 + 100 * 5 / 2 + 20"
    TOKENS = SENTENCE.split(" ")
    print(TOKENS)
    addhandler = AdditionHandler()
    subtracthandler = SubtractionHandler()
    multiplyhandler = MultiplicationHandler()
    dividehandler = DivisionHandler()

    # Make handler chain
    multiplyhandler.set_next(dividehandler).set_next(addhandler).set_next(subtracthandler)

    # Activate client code
    AST_ROOT = client_code(multiplyhandler, TOKENS)

    # Print out a representation of the AST_ROOT
    print(AST_ROOT)
    print(AST_ROOT.interpret())

    ####################################################################################################################
    # Workshop task make adapter pattern implementation, that will fix NumberOTHER' object has no attribute 'interpret'
    # How you do, it your thing:)
