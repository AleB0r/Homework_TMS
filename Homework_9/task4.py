import re


def censor_text(input_text, stop_words):
    with open(input_text, 'r', encoding='utf-8') as file:
        text = file.read()

    with open(stop_words, 'r', encoding='utf-8') as file:
        forbidden_words = file.read().split()

    forbidden_words = [word.lower() for word in forbidden_words]

    # Цензурирование текста
    censored_text = text
    for word in forbidden_words:
        pattern = re.escape(word)
        censored_text = re.sub(pattern, '*' * len(word), censored_text, flags=re.IGNORECASE)

    return censored_text


input_file = ("input_text.txt")
stop_words_file = "stop_words.txt"

censored_text = censor_text(input_file, stop_words_file)
print(censored_text)
