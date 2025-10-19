def calculate_student_grades(students, subjects, grades):
    subject_averages = {}

    for i, subject in enumerate(subjects):
        subject_grades = []
        for student_grades in grades:
            if i < len(student_grades):
                subject_grades.append(student_grades[i])
        if subject_grades:
            subject_averages[subject] = sum(subject_grades) / len(subject_grades)

    student_totals = []
    for i, student in enumerate(students):
        if i < len(grades):
            student_total = sum(grades[i])
            student_average = student_total / len(grades[i]) if grades[i] else 0
            student_totals.append((student, student_total, round(student_average, 2)))

    top_student = max(student_totals, key=lambda x: x[2]) if student_totals else ("", 0, 0)

    return {
        'subject_averages': subject_averages,
        'student_results': student_totals,
        'top_student': top_student
    }


def print_results(results):
    print("Средние баллы по предметам:")
    for subject, avg in results['subject_averages'].items():
        print(f"{subject}: {avg:.2f}")

    print("\nРезультаты студентов:")
    for student, total, avg in results['student_results']:
        print(f"{student}: сумма = {total}, средний = {avg}")

    print(f"\nЛучший студент: {results['top_student'][0]} со средним баллом {results['top_student'][2]}")


students1 = ["Иван", "Мария", "Петр"]
subjects1 = ["Математика", "Физика", "Химия"]
grades1 = [
    [5, 4, 3],
    [4, 5, 5],
    [3, 4, 4]
]

students2 = ["Анна", "Сергей"]
subjects2 = ["История", "Литература"]
grades2 = [
    [5, 5],
    [4, 3]
]

students3 = ["Ольга"]
subjects3 = ["Биология", "География", "Английский"]
grades3 = [
    [5, 4, 5]
]

print("ТЕСТ 1:")
result1 = calculate_student_grades(students1, subjects1, grades1)
print_results(result1)

print("\n" + "=" * 50)
print("ТЕСТ 2:")
result2 = calculate_student_grades(students2, subjects2, grades2)
print_results(result2)

print("\n" + "=" * 50)
print("ТЕСТ 3:")
result3 = calculate_student_grades(students3, subjects3, grades3)
print_results(result3)
