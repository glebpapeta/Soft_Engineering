def load_banned_words(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            banned_words = content.split()
        return banned_words
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def censor_text(text, banned_words):

    if not banned_words:
        return text

    result = text

    for banned_word in banned_words:

        import re
        pattern = re.compile(re.escape(banned_word), re.IGNORECASE)

        stars = '*' * len(banned_word)
        result = pattern.sub(stars, result)

    return result


def main():
    banned_words = load_banned_words('input.txt')

    if not banned_words:
        print("Нет запрещенных слов для обработки")
        return

    print(f"Запрещенные слова: {banned_words}")
    print("-" * 50)

    text = input("Введите предложение для проверки: ")

    print("\nОригинальный текст:")
    print(text)

    censored_text = censor_text(text, banned_words)

    print("\nРезультат после цензуры:")
    print(censored_text)


if __name__ == "__main__":
    main()
