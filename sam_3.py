def count_top_three_digits(digit_string):

    digit_count = {}

    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))

    top_three = dict(sorted_digits[:3])

    print("Три самые частые цифры (в порядке возрастания ключа):")
    for digit in sorted(top_three.keys()):
        print(f"Цифра {digit}: встречается {top_three[digit]} раз")

    return top_three

test_string = "123456789012345678901234567890"
print(f"Исходная строка: {test_string}")

result = count_top_three_digits(test_string)
print(f"\nСловарь с результатами: {result}")
