class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, num1, num2):
        if self.strategy is None:
            raise ValueError("Strategy is not set")

        return self.strategy.execute(num1, num2)


class Addition:
    def execute(self, num1, num2):
        return num1 + num2


class Subtraction:
    def execute(self, num1, num2):
        return num1 - num2


class Multiplication:
    def execute(self, num1, num2):
        return num1 * num2


class Division:
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2


if __name__ == "__main__":
    calculator = Calculator()

    calculator.set_strategy(Addition())
    result = calculator.calculate(5, 3)
    print(result)

    calculator.set_strategy(Subtraction())
    result = calculator.calculate(10, 4)
    print(result)

    calculator.set_strategy(Multiplication())
    result = calculator.calculate(6, 7)
    print(result)

    calculator.set_strategy(Division())
    result = calculator.calculate(20, 5)
    print(result)
