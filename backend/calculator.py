class Calculator:
    def __init__(self):
        self.stack = []

    def calculate(self, expression):
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y}

        tokens = expression.split()

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.stack.append(float(token))
            elif token in operators:
                if len(self.stack) < 2:
                    raise ValueError("Invalid expression")
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = operators[token](operand1, operand2)
                self.stack.append(result)
            else:
                raise ValueError("Invalid token: {}".format(token))

        if len(self.stack) == 1:
            return self.stack[0]
        else:
            raise ValueError("Invalid expression")