"""
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверить его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyOwnZeroDivisionError(Exception):
    def __init__(self, txt="Деление на ноль!!!"):
        self.txt = txt


def my_func(a, b):
    if b == 0:
        raise MyOwnZeroDivisionError("You give negative!")
    return a / b


try:
    print(my_func(1, 0))
except MyOwnZeroDivisionError as err:
    print(err)
