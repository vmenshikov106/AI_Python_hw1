"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, datestring):
        self.datestring = datestring

    @classmethod
    def chislo(cls, date: "Data"):
        return list(map(int, date.datestring.split("-")))

    @staticmethod
    def validation(date: "Data"):
        parsed_data = date.datestring.split("-")
        if len(parsed_data[2]) not in {2, 4}:
            raise ValueError("Невалидный год")
        if not 1 <= int(parsed_data[1]) <= 12:
            raise ValueError("Невалидный месяц")
        if not 1 <= int(parsed_data[0]) <= 31:
            raise ValueError("Невалидное число")
        print("Валидация пройдена успешно")


date = Data("10-01-2020")
date.validation(date)
print(Data.chislo(date))
