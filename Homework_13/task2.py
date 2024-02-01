def cyclic_sequence(*args, n):
    i = 0
    while i < n:
        yield args[i % len(args)]
        i += 1

numbers_list = input("Введите числа через пробел для циклической последовательности: ").split()
n = int(input("Введите количество чисел для вывода: "))

gen = cyclic_sequence(*numbers_list, n=n)
for number in gen:
    print(number)
