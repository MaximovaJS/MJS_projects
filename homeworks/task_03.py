# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

while True:
    user_input = input("Введите номер месяца: ")
    month = int(user_input)
    print('Вы ввели', month)
    len_month=[31,28,31,30,31,30,31,31,30,31,30,31]

    if month>0 and month<13:
        print('В', month,'месяце число дней равно', len_month[month-1])
        break
    
    else:
        print('Такого месяца не существует')
# Отлично, вот еще решение
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
