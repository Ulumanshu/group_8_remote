# pylint: disable=too-few-public-methods
"The Interpreter Pattern Concept"


class AbstractExpression():
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
        self.value = int(value)

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


class Multiply(AbstractExpression):
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
        return self.left.interpret() / self.right.interpret()

    def __repr__(self):
        return f"({self.left} Divide {self.right})"


# The Client
# The sentence complies with a simple grammar of
# Number -> Operator -> Number -> etc,
SENTENCE = "5 + 4 - 3 + 7 - 2"
print(SENTENCE)

# Split the sentence into individual expressions that will be added to
# an Abstract Syntax Tree (AST) as Terminal and Non-Terminal expressions
TOKENS = SENTENCE.split(" ")
print(TOKENS)

# Si Dalis negrazi ir manualine
# sukurti client_code funkcija, panasia i chain_of_responsibility faile esancia
# ji turetu eiti per tokenus ir skumonpiliuoti AST kur pagal chain of responsibility paterna
# bus parenkamas teisingas handleris tokenui, kuris i AST lista ikels teisinga objekta
# grazins paskutini AST elementa

##########################################################################################
# Manually Creating an Abstract Syntax Tree from the tokens
# AST: list[AbstractExpression] = []  # Python 3.9
AST = []  # Python 3.8 or earlier
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))  # 5 + 4
AST.append(Subtract(AST[0], Number(TOKENS[4])))        # ^ - 3
AST.append(Add(AST[1], Number(TOKENS[6])))             # ^ + 7
AST.append(Subtract(AST[2], Number(TOKENS[8])))        # ^ - 2

# Use the final AST row as the root node.
AST_ROOT = AST.pop()
#############################################################################################


# Interpret recursively through the full AST starting from the root.
print(AST_ROOT.interpret())

# Print out a representation of the AST_ROOT
print(AST_ROOT)

SENTENCE2 = "5 + 9 / 3"
TOKENS2 = SENTENCE2.split(" ")

AST = []
AST.append(Add(Number(TOKENS2[0]), Number(TOKENS2[2])))  # 5 + 4
AST.append(Divide(AST[0], Number(TOKENS2[4])))           # ^ / 3

AST_ROOT = AST.pop()

print(AST_ROOT.interpret())
print(AST_ROOT)
