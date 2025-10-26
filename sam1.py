from collections import Counter


def count_words_and_find_most_common(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        punctuation = '.,!?;:"()—«»'
        for char in punctuation:
            text = text.replace(char, '')

        words = text.lower().split()
        word_count = len(words)

        word_freq = Counter(words)
        most_common_word, frequency = word_freq.most_common(1)[0]

        return word_count, most_common_word, frequency

    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
        return None, None, None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None, None


def main():
    filename = "input.txt"

    word_count, most_common_word, frequency = count_words_and_find_most_common(filename)

    if word_count is not None:
        print(f"Количество слов в файле: {word_count}")
        print(f"Самое часто встречающееся слово: '{most_common_word}'")
        print(f"Количество повторений: {frequency}")


if __name__ == "__main__":
    main()
