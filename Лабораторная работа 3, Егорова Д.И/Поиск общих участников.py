def find_common_participants(participants_first_group, participants_second_group, delimiter=","):
    # Разбиваем строки на списки участников, используя заданный разделитель
    participants_list_1 = participants_first_group.split(delimiter)
    participants_list_2 = participants_second_group.split(delimiter)

    # Преобразуем списки во множества для более эффективной проверки пересечения
    set_1 = set(participants_list_1)
    set_2 = set(participants_list_2)

    # Находим общих участников
    common_participants = set_1.intersection(set_2)

    # Преобразуем результат обратно в список и сортируем его
    common_participants_list = sorted(list(common_participants))

    return common_participants_list

# Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(common_participants)