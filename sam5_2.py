results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)

print("=== АНАЛИЗ РЕЗУЛЬТАТОВ БЕГА ===")
print(f"Все результаты: {results}")
print(f"Отсортированные результаты: {sorted_results}")
print()

print("Три лучшие результата:")
for i, result in enumerate(sorted_results[:3], 1):
    print(f"  {i} место: {result} сек")

print()

print("Три худшие результата:")
for i, result in enumerate(sorted_results[-3:][::-1], 1):
    print(f"  {i} место с конца: {result} сек")

print()

print("Все результаты начиная с 10-го места:")
for i, result in enumerate(sorted_results[9:], 10):
    print(f"  {i} место: {result} сек")

print()
print("=== СВОДНАЯ ИНФОРМАЦИЯ ===")
print(f"Общее количество результатов: {len(results)}")
print(f"Лучший результат: {min(results)} сек")
print(f"Худший результат: {max(results)} сек")
print(f"Средний результат: {sum(results)/len(results):.1f} сек")
