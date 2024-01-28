def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

number = int(input("Введите количество чисел в последовательности: "))

for num in fibonacci_sequence(number):
    print(num)