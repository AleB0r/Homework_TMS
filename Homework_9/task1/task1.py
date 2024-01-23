import os
import shutil
import sys


def get_os_name():
    return os.name


def get_current_directory():
    return os.getcwd()


def sort_files_by_extension(directory):
    files = os.listdir(directory)
    extensions = set()

    # Собираем список уникальных расширений файлов
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            _, extension = os.path.splitext(file)
            extensions.add(extension)

    # Создаем поддиректории для каждого расширения
    for extension in extensions:
        folder_name = extension[1:]  # Удаляем точку из расширения
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Перемещаем файлы в соответствующие поддиректории
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            _, extension = os.path.splitext(file)
            folder_name = extension[1:]  # Удаляем точку из расширения
            folder_path = os.path.join(directory, folder_name)
            file_path = os.path.join(directory, file)
            shutil.move(file_path, folder_path)
    return True

def rename_file(directory, file_name, new_file_name):
    file_path = os.path.join(directory, file_name)
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(file_path, new_file_path)
    return True


def main():
    if len(sys.argv) < 2:
        print("Необходимо указать имя файла как аргумент командной строки.")
        return

    file_to_rename = sys.argv[1]

    try:
        # Вывод имени операционной системы
        os_name = get_os_name()
        print("Имя операционной системы:", os_name)

        # Вывод текущей директории
        current_directory = get_current_directory()
        print("Текущая директория:", current_directory)

        # Переименование файла
        new_file_name = "new_data.txt"
        if rename_file(current_directory, file_to_rename, new_file_name) == True:
            print(f"Файл {file_to_rename} был переименован в {new_file_name}.")

        # Рассортировка файлов по расширениям
        if sort_files_by_extension(current_directory) == True:
            print("Файлы успешно рассортированы по расширениям.")
    except FileNotFoundError:
        print(f"Файл {file_to_rename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")




if __name__ == "__main__":
    main()