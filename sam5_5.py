def create_special_set(numbers):
   
    result_set = set()

    from collections import Counter
    count_dict = Counter(numbers)

    for number, count in count_dict.items():
        result_set.add(number)

        if count > 1:
            for repeat_count in range(2, count + 1):
                repeated_str = str(number) * repeat_count
                result_set.add(repeated_str)

    return result_set


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print("=== ФОРМИРОВАНИЕ МНОЖЕСТВ С ПРЕОБРАЗОВАНИЕМ ПОВТОРОВ ===")
print("Правило: если число повторяется n раз, то добавляем:")
print("  - само число")
print("  - строки: число×2, число×3, ..., число×n")
print()

print("list_1 =", list_1)
set_1 = create_special_set(list_1)
print("Множество 1:", set_1)
print()

print("list_2 =", list_2)
set_2 = create_special_set(list_2)
print("Множество 2:", set_2)
print()

print("list_3 =", list_3)
set_3 = create_special_set(list_3)
print("Множество 3:", set_3)
print()

print("=== ПОДРОБНЫЙ АНАЛИЗ ПРЕОБРАЗОВАНИЙ ===")


def detailed_analysis(numbers, set_name):
    from collections import Counter
    count_dict = Counter(numbers)
    print(f"\n{set_name}:")
    for number, count in count_dict.items():
        if count == 1:
            print(f"  Число {number}: встречается 1 раз -> добавляем только {number}")
        else:
            additions = [number] + [str(number) * i for i in range(2, count + 1)]
            print(f"  Число {number}: встречается {count} раз -> добавляем {additions}")


detailed_analysis(list_1, "list_1")
detailed_analysis(list_2, "list_2")
detailed_analysis(list_3, "list_3")
