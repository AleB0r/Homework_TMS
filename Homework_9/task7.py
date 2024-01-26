def caesar_cipher(text, step):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + step) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + step) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text


input_file = "cezar.txt"
output_file = "encrypted_output.txt"

with open(input_file, 'r') as file:
    lines = file.readlines()

encrypted_lines = []
for i, line in enumerate(lines):
    step = i + 1
    encrypted_line = caesar_cipher(line.strip(), step)
    encrypted_lines.append(encrypted_line)

output_text = ' '.join(encrypted_lines)

with open(output_file, 'w') as file:
    file.write(output_text)

print("Текст успешно зашифрован и сохранен в файле", output_file)
