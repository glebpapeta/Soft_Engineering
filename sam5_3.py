import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print("Исходные списки:")
print(f"one = {one}")
print(f"two = {two}")
print(f"three = {three}")
print()

def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return None

min_one = min(one)
min_two = min(two)
min_three = min(three)

max_one = max(one)
max_two = max(two)
max_three = max(three)

print("Минимальные элементы:")
print(f"min_one = {min_one}, min_two = {min_two}, min_three = {min_three}")
print("Максимальные элементы:")
print(f"max_one = {max_one}, max_two = {max_two}, max_three = {max_three}")
print()

triangle_min = [min_one, min_two, min_three]
triangle_max = [max_one, max_two, max_three]

print("Треугольник из минимальных элементов:", triangle_min)
print("Треугольник из максимальных элементов:", triangle_max)
print()

area_min = calculate_triangle_area(min_one, min_two, min_three)
area_max = calculate_triangle_area(max_one, max_two, max_three)

print("=== РЕЗУЛЬТАТЫ ===")
if area_min is not None:
    print(f"Площадь треугольника из минимальных элементов: {area_min:.2f}")
else:
    print("Треугольник из минимальных элементов не существует!")

if area_max is not None:
    print(f"Площадь треугольника из максимальных элементов: {area_max:.2f}")
else:
    print("Треугольник из максимальных элементов не существует!")

print("\n=== ПРОВЕРКА УСЛОВИЙ СУЩЕСТВОВАНИЯ ТРЕУГОЛЬНИКОВ ===")
print(f"Треугольник мин: {min_one} + {min_two} = {min_one + min_two} > {min_three} -> {min_one + min_two > min_three}")
print(f"Треугольник макс: {max_one} + {max_two} = {max_one + max_two} > {max_three} -> {max_one + max_two > max_three}")
