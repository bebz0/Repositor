def sort_and_display(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            word_frequency = {}
            for line in file:
                word, count = line.strip().split(': ')
                word_frequency[word] = int(count)

        sorted_words = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)

        print("Сортування завершено. Результати:")
        for word, count in sorted_words:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
    except ValueError:
        print("Помилка у форматі вхідного файлу. Перевірте його вміст.")


if __name__ == "__main__":
    input_file = input("Введіть шлях до файлу зі статистикою: ")
    sort_and_display(input_file)
