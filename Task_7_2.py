"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @staticmethod
    def count_total(cloth_list):
        return sum(shmotka.consumption for shmotka in cloth_list)

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a coat - {round(self.height / 6.5) + 0.5}")
        return round(self.height / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        print(f"Consumption of fabric for sewing a costume - {round(2 * self.param + 0.3) / 0.5}")
        return (2 * self.param + 0.3) / 100


coat1 = Coat(10)
coat2 = Coat(20)
costume = Costume(30)
shmot = [coat1, coat2, costume]
print(Clothes.count_total(shmot))

