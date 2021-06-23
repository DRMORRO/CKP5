# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ
# к отдельным полям через методы класса.

class Car:
    def __init__(self, model: str, year: int, manufacturer: str, engine_volume: int, color: str, price: int):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_engine_volume(self):
        return self.engine_volume

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
