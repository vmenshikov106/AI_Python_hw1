"""4) Реализовать базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    __compass = {0: "Север",
                 1: "Восток",
                 2: "Юг",
                 3: "Запад"}

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.condition = {"is_moving": False, "direction": 0}

    def go(self):
        self.condition["is_moving"] = True

    def stop(self):
        self.condition["is_moving"] = False

    def turn(self, direction):
        if direction.lower() not in {"left", "right"}:
            raise ValueError("Введите корректное значение поворота")
        elif direction == "left":
            self.condition["direction"] = (self.condition["direction"] + 3) % 4
        elif direction == "right":
            self.condition["direction"] = (self.condition["direction"] + 5) % 4

    def show_speed(self):
        return {"speed": self.speed, "massages": []}

    def show_direction(self):
        return Car.__compass[self.condition["direction"]]

class AbstractVillageCar(Car):
    speed_limit = 0

    def show_speed(self):
        speed_info = super().show_speed()
        if speed_info["speed"] > self.speed_limit:
            speed_info["massages"].append("Вы превышаете допустимую скорость!")
        return speed_info

class TownCar(AbstractVillageCar):
    speed_limit = 60

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class WorkCar(AbstractVillageCar):
    speed_limit = 40

car = WorkCar(speed=120, color="red", name="dodge", is_police=False)
car.turn("left")
print(car.show_direction())
car.turn("right")
print(car.show_direction())
car.turn("left")
print(car.show_direction())
car.turn("right")
print(car.show_direction())
car.turn("left")
print(car.show_direction())
car.turn("left")
print(car.show_direction())
car.turn("left")
print(car.show_direction())

print(car.show_speed())

