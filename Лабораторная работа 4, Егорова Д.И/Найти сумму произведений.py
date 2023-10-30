import json

def task() -> float:
    # Открываем файл с данными JSON
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Инициализируем переменную для хранения суммы произведений
    total_product = 0.0

    # Проходим по каждому словарю в списке
    for entry in data:
        score = entry.get("score", 0)  # Получаем значение "score" из словаря (по умолчанию 0, если ключ отсутствует)
        weight = entry.get("weight", 0)  # Получаем значение "weight" из словаря (по умолчанию 0, если ключ отсутствует)
        product = score * weight  # Вычисляем произведение
        total_product += product  # Добавляем произведение к общей сумме

    # Округляем сумму до 3 знаков после запятой
    rounded_total_product = round(total_product, 3)

    return rounded_total_product

# Вызываем функцию и выводим результат
result = task()
print(result)





