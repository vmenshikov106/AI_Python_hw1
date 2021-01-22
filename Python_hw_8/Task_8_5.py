"""
5. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число», реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)

    def __str__(self):
        znak = ""
        if self.b > 0:
            znak = "+"
        return f'z = {self.a} {znak}{self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
