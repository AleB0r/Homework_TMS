def find_low_grades(lines):
    low_grades_students = []

    for line in lines:
        surname, name, grade = line.strip().split()
        if int(grade) < 3:
            low_grades_students.append(f"{surname} {name}")

    return low_grades_students

if __name__ == "__main__":
    file_name = "students.txt"

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    low_grades_students = find_low_grades(lines)

    if low_grades_students:
        print("Ученики с оценкой меньше 3:")
        for student in low_grades_students:
            print(student)
    else:
        print("Нет учеников с оценкой меньше 3.")