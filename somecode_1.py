class OwnError(Exception):  # создание дочернего класса обработки исключений
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите неотрицательное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError("Вы ввели отрицательное число!")  # вызов класса обработки исключений
except ValueError:
    print("Вы ввели не число")
except OwnError as err:  # обработка исключения
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")
