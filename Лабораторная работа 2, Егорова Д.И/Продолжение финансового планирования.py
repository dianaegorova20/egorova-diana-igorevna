salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Изначальная подушка безопасности

for month in range(months):
    money_capital += salary  # Добавляем зарплату
    money_capital -= spend  # Вычитаем расходы
    spend = spend * (1 + increase)  # Учитываем рост цен на расходы

money_capital = abs(round(money_capital))  # Округляем до целого числа

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")