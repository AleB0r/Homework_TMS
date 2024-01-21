class Math:
    def addition(self, num1, num2):
        result = num1 + num2
        print(f"Результат сложения: {result}")

    def subtraction(self, num1, num2):
        result = num1 - num2
        print(f"Результат вычитания: {result}")

    def multiplication(self, num1, num2):
        result = num1 * num2
        print(f"Результат умножения: {result}")

    def division(self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            print(f"Результат деления: {result}")
        else:
            print("Ошибка: деление на ноль недопустимо!")


math = Math()

math.addition(5, 3)
math.subtraction(10, 4)
math.multiplication(2, 6)
math.division(10, 2)
math.division(8, 0)