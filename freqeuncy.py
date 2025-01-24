def count_word_frequency(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            words = file.read().split()

        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        with open(output_path, 'w', encoding='utf-8') as output_file:
            for word, count in word_frequency.items():
                output_file.write(f"{word}: {count}\n")

        print(f"Підрахунок завершено. Результат збережено в {output_path}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")


if __name__ == "__main__":
    input_file = input("Введіть шлях до очищеного текстового файлу: ")
    output_file = input("Введіть шлях для збереження статистики: ")
    count_word_frequency(input_file, output_file)
