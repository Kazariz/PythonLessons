class Car:
    def __init__(self):
        self._model = None
        self._year = None
        self._manufacturer = None
        self._engine_power = None
        self._color = None
        self._price = None

    def input_data(self, model, year, manufacturer, engine_power, color, price):
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_power = engine_power
        self._color = color
        self._price = price

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_manufacturer(self):
        return self._manufacturer

    def get_engine_power(self):
        return self._engine_power

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def display_info(self):
        print("********** Данные автомобиля **********")
        print(f"Название модели: {self._model}")
        print(f"Год выпуска: {self._year}")
        print(f"Производитель: {self._manufacturer}")
        print(f"Мощность двигателя: {self._engine_power} л.с.")
        print(f"Цвет машины: {self._color}")
        print(f"Цена: {self._price}")
        print("=======================================")


car = Car()
car.input_data("X7 M50i", 2021, "BMW", 530, "white", 10790000)
car.display_info()
