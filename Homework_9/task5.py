def find_low_grades(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    low_grades_students = []
    for line in lines:
        # Разделение строки на фамилию, имя и оценку
        surname, name, grade = line.strip().split()
        # Проверка оценки
        if int(grade) < 3:
            # Добавление ученика с низкой оценкой в список
            low_grades_students.append(f"{surname} {name}")

    return low_grades_students


file_name = "students.txt"

low_grades_students = find_low_grades(file_name)
if low_grades_students:
    print("Ученики с оценкой меньше 3:")
    for student in low_grades_students:
        print(student)
else:
    print("Нет учеников с оценкой меньше 3.")
