def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        lines = content.splitlines()
        line_count = len(lines)

        words = content.split()
        word_count = len(words)

        letter_count = 0
        for char in content:
            if char.isalpha() and char.isascii():
                letter_count += 1

        print("Input file contains:")
        print(f"{letter_count} letters")
        print(f"{word_count} words")
        print(f"{line_count} lines")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


def main():
    filename = "input.txt"
    analyze_text_file(filename)


if __name__ == "__main__":
    main()
