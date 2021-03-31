class Auto:

    def __init__(self, year):
        self.year = year

    @property  # свойство года
    def year(self):
        return self.__year

    @year.setter  # сеттер для создания свойств
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль был выпущен в {str(self.year)} году"

a = Auto(2090)
print(a.get_auto_year())
