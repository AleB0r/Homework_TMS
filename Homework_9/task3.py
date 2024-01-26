def find_most_common_word(line):
    words = line.split()

    if not words:
        return None, 0

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = None
    count = 0

    for word, word_count in word_counts.items():
        if word_count > count:
            most_common_word = word
            count = word_count

    return most_common_word, count



input_file = "input.txt"

output_file = "output.txt"


with open(input_file, 'r', encoding='utf-8') as file:

    with open(output_file, 'w', encoding='utf-8') as output:

        for line in file:

            clean_line = line.strip()


            most_common_word, count = find_most_common_word(clean_line)

            if most_common_word is None:
                continue

            output.write(f"{most_common_word}: {count}\n")
