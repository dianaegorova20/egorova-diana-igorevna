def count_letters(text):
    # Создаем пустой словарь для хранения частот букв нижнего регистра
    letter_count = {}

    # Проходим по каждому символу в тексте
    for char in text:
        # Проверяем, является ли символ буквой и переводим его в нижний регистр
        if char.isalpha():
            char = char.lower()
            # Если символ уже есть в словаре, увеличиваем его счетчик на 1, иначе добавляем его в словарь
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency_dict = {}

    for letter, count in letter_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = frequency

    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_count = count_letters(main_str)
frequency_dict = calculate_frequency(letter_count)

# Выводим словарь с частотами букв
for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")


