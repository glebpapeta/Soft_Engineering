def fix_grades(grades):

    fixed_grades = []
    for grade in grades:
        if grade == 3:
            fixed_grades.append(4)
        elif grade != 2:
            fixed_grades.append(grade)

    return fixed_grades


grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("=== ОБРАБОТКА ОЦЕНОК СТУДЕНТА ===")
print("Правила:")
print("- Все двойки удаляются")
print("- Все тройки заменяются на четверки")
print()

print("Список 1:")
print(f"Исходный: {grades_list_1}")
fixed_1 = fix_grades(grades_list_1)
print(f"Исправленный: {fixed_1}")
print(f"Статистика: удалено {len(grades_list_1) - len(fixed_1)} двоек, "
      f"заменено {grades_list_1.count(3)} троек")
print()

print("Список 2:")
print(f"Исходный: {grades_list_2}")
fixed_2 = fix_grades(grades_list_2)
print(f"Исправленный: {fixed_2}")
print(f"Статистика: удалено {len(grades_list_2) - len(fixed_2)} двоек, "
      f"заменено {grades_list_2.count(3)} троек")
print()

print("Список 3:")
print(f"Исходный: {grades_list_3}")
fixed_3 = fix_grades(grades_list_3)
print(f"Исправленный: {fixed_3}")
print(f"Статистика: удалено {len(grades_list_3) - len(fixed_3)} двоек, "
      f"заменено {grades_list_3.count(3)} троек")
print()

print("=== СВОДНАЯ СТАТИСТИКА ===")
all_original = grades_list_1 + grades_list_2 + grades_list_3
all_fixed = fixed_1 + fixed_2 + fixed_3

print(f"Всего оценок в исходных списках: {len(all_original)}")
print(f"Всего оценок после обработки: {len(all_fixed)}")
print(f"Удалено двоек всего: {all_original.count(2)}")
print(f"Заменено троек всего: {all_original.count(3)}")
print(f"Средний балл до обработки: {sum(all_original) / len(all_original):.2f}")
print(f"Средний балл после обработки: {sum(all_fixed) / len(all_fixed):.2f}")
