'''

12. (МОДУЛЬ 5) В проекте создать новый модуль borndayforewer.py
13.Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:
Просим пользователя ввести год рождения А.С. Пушкина до тех пор пока он не ввел правильный год,
после этого спрашиваем день рождения до тех пор, пока он не ввел верный день.
После верного ответа выводим в терминал 'Верно' и выходим из программы

'''

while int(input("Введите год рождения Пушкина\n")) != 1799:
    print("Неверный год рождения")
while int(input("Введите день рождения Пушкина\n")) != 26:
    print("Неверный день рождения")
print("Верно")
