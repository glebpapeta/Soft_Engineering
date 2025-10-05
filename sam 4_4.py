def calculate_average(*args):
    """
    Функция для вычисления среднего арифметического произвольного количества аргументов.

    Args:
        *args: Произвольное количество числовых аргументов

    Returns:
        float: Среднее арифметическое значение
    """
    if len(args) == 0:
        return 0

    total_sum = sum(args)

    average = total_sum / len(args)

    return average


if __name__ == '__main__':
    result1 = calculate_average(1, 2, 3, 4, 5)
    print(f"Среднее арифметическое (1, 2, 3, 4, 5): {result1}")

    result2 = calculate_average(10, 20, 30)
    print(f"Среднее арифметическое (10, 20, 30): {result2}")

    result3 = calculate_average(2.5, 3.7, 1.8, 4.2)
    print(f"Среднее арифметическое (2.5, 3.7, 1.8, 4.2): {result3}")

    result4 = calculate_average()
    print(f"Среднее арифметическое без аргументов: {result4}")
