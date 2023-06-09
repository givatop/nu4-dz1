from typing import List
from collections import namedtuple

"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

Purchase = namedtuple('Purchase', 'name amount')
history = []  # type: List[Purchase]
account = 0


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    new_purchase = None
    if choice == '1':
        amount = int(input("На какую сумму Вы хотите пополнить счет: "))
        account += amount
        print()

    elif choice == '2':
        amount = int(input("Введите сумму покупки: "))
        if amount > account:
            print("Недостаточно средств\n")
            continue
        name = input("Введите название покупки: ")
        account -= amount
        history.append(Purchase(name, amount))
        print()

    elif choice == '3':
        [print(f'{name} {amount}') for (name, amount) in history]
        print()

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню\n')
