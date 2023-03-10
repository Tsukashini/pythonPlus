"""
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз
(Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки
пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

"""
import random

famous_people = {'Пушкина': '06.06.1799', 'Лермонтова': '15.10.1814', 'Носова': '23.11.1908',
                 'Тютчева': '05.12.1803', 'Достоевского': '11.11.1821', 'Тургенева': '09.10.1818',
                 'Булгакова': '15.05.1891', 'Ахматовой': '23.06.1889', 'Маяковского': '19.07.1893',
                 'Толстого': '09.09.1828'
                 }

days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
        '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двенадцатое',
        '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
        '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое',
        '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',
        '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое',
        '30': 'тридцатое', '31': 'тридцать первое'
        }

months = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
          '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
          }

q = 1

while q != 0:

    success = 0

    for key, value in random.sample(famous_people.items(), 5):
        if input("Введите дату рождения {}\n".format(key)) == value:
            success += 1
        else:
            day, month, year = value.split(sep='.')
            print('{} {} {} года'.format(days.get(day), months.get(month), year))

    print("Количество правильных ответов:", success)
    print("Количество ошибок:", 5-success)
    if input("Начать заново? да/нет \n") != 'да':
        q = 0
