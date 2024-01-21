from collections import Counter


def find_most_common_word(line):
    words = line.split()

    if not words:
        return None, 0

    word_counts = Counter(words)

    most_common_word, count = word_counts.most_common(1)[0]

    return most_common_word, count


# Имя входного файла
input_file = "input.txt"
# Имя выходного файла
output_file = "output.txt"

# Чтение текста из файла
with open(input_file, 'r', encoding='utf-8') as file:
    # Создание выходного файла
    with open(output_file, 'w', encoding='utf-8') as output:
        # Чтение каждой строки из входного файла
        for line in file:
            # Очистка строки от лишних символов (пробелов, знаков пунктуации)
            clean_line = line.strip()

            # Поиск наиболее часто встречающегося слова и его счетчика
            most_common_word, count = find_most_common_word(clean_line)

            if most_common_word is None:
                continue

            output.write(f"{most_common_word}: {count}\n")
