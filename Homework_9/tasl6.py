import re


def sum_numbers(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    numbers = re.findall(r'\d+', content)

    total_sum = sum(map(int, numbers))

    return total_sum


file_name = "number.txt"
total_sum = sum_numbers(file_name)
print("Сумма всех чисел:", total_sum)
