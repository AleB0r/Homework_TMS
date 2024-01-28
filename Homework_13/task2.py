def cyclic_sequence(*args):
    while True:
        for num in args:
            yield num

numbers_list = input("Введите числа через пробел для циклической последовательности: ").split()
n = int(input("Введите количество чисел для вывода: "))

gen = cyclic_sequence(*numbers_list)
for _ in range(n):
    print(next(gen))