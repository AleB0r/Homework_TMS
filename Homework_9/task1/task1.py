import os
import shutil


def sort_files_by_extension(folder_path):
    files = os.listdir(folder_path)

    extensions = set(os.path.splitext(file)[1] for file in files)
    for extension in extensions:
        os.makedirs(os.path.join(folder_path, extension.lstrip('.')), exist_ok=True)

    for file in files:
        extension = os.path.splitext(file)[1].lstrip('.')
        if extension:
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(folder_path, extension, file)
            shutil.move(source_path, destination_path)


def rename_file(file_path, new_name):
    file_name = os.path.basename(file_path)

    folder_path = os.path.dirname(file_path)

    new_path = os.path.join(folder_path, new_name)

    os.rename(file_path, new_path)

    return new_path


# Вывод имени операционной системы
print("Имя операционной системы:", os.name)

# Вывод пути к текущей папке
print("Путь к текущей папке:", os.getcwd())

folder_path = os.getcwd()

sort_files_by_extension(folder_path)

# Вывод информации о перемещенных файлах
for root, dirs, files in os.walk(folder_path):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        file_count = len(os.listdir(dir_path))
        total_size = sum(os.path.getsize(os.path.join(dir_path, file)) for file in os.listdir(dir_path))
        print(f"В папке {dir_path} перемещено {file_count} файлов, их суммарный размер - {total_size} байт")

file_to_rename = os.path.join(folder_path, "txt", "data.txt")
new_file_name = "data.txt"
new_file_path = rename_file(file_to_rename, new_file_name)
print(f"Файл {file_to_rename} был переименован в {new_file_path}")
