"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки”.
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def draw(self):
        return "Рисуем"

class Pen(Stationery):
    def draw(self):
        return f"{super().draw()} ручкой"

class Pencil(Stationery):
    def draw(self):
        return f"{super().draw()} карандашом"

class Handle(Stationery):
    def draw(self):
        return f"{super().draw()} маркером"

pen = Pen()
print(pen.draw())