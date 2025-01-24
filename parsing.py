def parse_and_clean_text(file_path, output_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        unwanted_chars = ".,!@#$%^&*()[]{}:;\"'<>?/\\|`~_-+=1234567890"
        clean_text = ''.join(char.lower() if char not in unwanted_chars else ' ' for char in text)
        words = clean_text.split()

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(words))

        print(f"Обробка завершена. Результат збережено в {output_path}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")


if __name__ == "__main__":
    input_file = input("Введіть шлях до вхідного текстового файлу: ")
    output_file = input("Введіть шлях для збереження результату: ")
    parse_and_clean_text(input_file, output_file)
