import json
import csv


# Задание 0
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Задание 1
def convert_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())  # Записываем заголовки
        for row in data:
            writer.writerow(row.values())


# Задание 2
def save_to_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row.values())


# Задание 3
def add_employee_to_json(json_file_path):
    new_employee = {}
    new_employee["name"] = input("Введите имя сотрудника: ")
    new_employee["birthday"] = input("Введите дату рождения сотрудника: ")
    new_employee["height"] = int(input("Введите рост сотрудника: "))
    new_employee["weight"] = float(input("Введите вес сотрудника: "))
    new_employee["car"] = input("Есть ли у сотрудника автомобиль (да/нет): ").lower() == "да"
    languages = input("Введите языки программирования через запятую: ")
    new_employee["languages"] = [language.strip() for language in languages.split(",")]

    with open(json_file_path, 'r+') as file:
        data = json.load(file)
        data.append(new_employee)
        file.seek(0)
        json.dump(data, file, indent=4)


# Задание 4
def add_employee_to_csv(csv_file_path):
    new_employee = {}
    new_employee["name"] = input("Введите имя сотрудника: ")
    new_employee["birthday"] = input("Введите дату рождения сотрудника: ")
    new_employee["height"] = int(input("Введите рост сотрудника: "))
    new_employee["weight"] = float(input("Введите вес сотрудника: "))
    new_employee["car"] = input("Есть ли у сотрудника автомобиль (да/нет): ").lower() == "да"
    languages = input("Введите языки программирования через запятую: ")
    new_employee["languages"] = [language.strip() for language in languages.split(",")]

    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_employee.values())


# Задание 5
def search_employee_by_name(data):
    name = input("Введите имя сотрудника для поиска: ")
    for employee in data:
        if employee["name"] == name:
            print("Найден сотрудник:")
            print("Имя:", employee["name"])
            print("Дата рождения:", employee["birthday"])
            print("Рост:", employee["height"])
            print("Вес:", employee["weight"])
            print("Наличие автомобиля:", employee["car"])
            print("Языки программирования:", ", ".join(employee["languages"]))
            return
    print("Сотрудник с таким именем не найден.")


# Задание 6
def filter_by_language(data):
    languages = input("Введите языки программирования для фильтрации (через запятую): ")
    filter_languages = [language.strip() for language in languages.split(",")]
    filtered_employees = []
    for employee in data:
        for language in filter_languages:
            if language in employee["languages"]:
                filtered_employees.append(employee.copy())
                break

    print("Сотрудники, владеющие языками программирования:", ", ".join(filter_languages))
    for employee in filtered_employees:
        print("Имя:", employee["name"])
        print("Дата рождения:", employee["birthday"])
        print("Рост:", employee["height"])
        print("Вес:", employee["weight"])
        print("Наличие автомобиля:", employee["car"])
        print("Языки программирования:", ", ".join(employee["languages"]))


# Задание 7
def filter_by_year(data):
    year = int(input("Введите год рождения для фильтрации: "))
    total_height = 0
    count = 0
    for employee in data:
        if int(employee["birthday"].split(".")[2]) < year:
            count += 1
            total_height += employee["height"]

    if count > 0:
        average_height = total_height / count
        print("Средний рост сотрудников, родившихся до", year, "года:", average_height)
    else:
        print("Нет сотрудников, родившихся до", year, "года.")


# Задание 8
def interactive_menu(json_file_path, csv_file_path):
    while True:
        print("\nМеню:")
        print("1. Преобразовать JSON в CSV")
        print("2. Сохранить данные в CSV")
        print("3. Добавить сотрудника в JSON")
        print("4. Добавить сотрудника в CSV")
        print("5. Поиск сотрудника по имени")
        print("6. Фильтр по языку программирования")
        print("7. Фильтр по году рождения")
        print("8. Выход\n")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            data = read_json_file(json_file_path)
            convert_to_csv(data, csv_file_path)
            print("Преобразование JSON в CSV выполнено.")
        elif choice == "2":
            data = read_json_file(json_file_path)
            save_to_csv(data, csv_file_path)
            print("Данные сохранены в CSV файле.")
        elif choice == "3":
            add_employee_to_json(json_file_path)
            print("Данные о новом сотруднике добавлены в JSON файл.")
        elif choice == "4":
            add_employee_to_csv(csv_file_path)
            print("Данные о новом сотруднике добавлены в CSV файл.")
        elif choice == "5":
            data = read_json_file(json_file_path)
            search_employee_by_name(data)
        elif choice == "6":
            data = read_json_file(json_file_path)
            filter_by_language(data)
        elif choice == "7":
            data = read_json_file(json_file_path)
            filter_by_year(data)
        elif choice == "8":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


# Пример использования
json_file_path = "data.json"
csv_file_path = "data.csv"

interactive_menu(json_file_path, csv_file_path)
