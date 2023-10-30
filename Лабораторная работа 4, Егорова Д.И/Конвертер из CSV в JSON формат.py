import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json(input_filename, output_filename):
    # Открываем CSV файл для чтения
    with open(input_filename, 'r') as csv_file:
        # Читаем CSV файл с заданными разделителями
        csv_reader = csv.DictReader(csv_file, delimiter=',', lineterminator='\n')

        # Создаем список для хранения записей в формате словаря
        records = []

        # Проходим по каждой записи в CSV файле
        for row in csv_reader:
            records.append(dict(row))  # Преобразуем строку CSV в словарь и добавляем его в список

        # Открываем JSON файл для записи с отступами
        with open(output_filename, 'w') as json_file:
            # Записываем список записей в JSON файл с отступами
            json.dump(records, json_file, indent=4)


if __name__ == '__main__':
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

