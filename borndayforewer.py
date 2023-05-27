"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def do_while_input_not_equal_value(value: str, input_question: str, wrong_answer_message='Не верно'):
    """
    Создает бесконечный цикл выходом из которой служит условие: input() == value.
    Пока пользователь не даст правильного ответа будет выводится сообщение wrong_answer_message.
    :param value:
    :param input_question: вопрос, который увидит пользователь: input(input_question)
    :param wrong_answer_message:
    :return: None
    """
    while input(input_question) != value:
        print(wrong_answer_message)


pushkin_bornyear = '1799'
pushkin_bornday = '6'
pushkin_bornyear_question = 'Ввведите год рождения А.С. Пушкина:'
pushkin_bornday_question = 'Ввведите день рождения А.С. Пушкина:'

do_while_input_not_equal_value(pushkin_bornyear, pushkin_bornyear_question)
do_while_input_not_equal_value(pushkin_bornday, pushkin_bornday_question)

print('Верно')
