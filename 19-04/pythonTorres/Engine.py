class Engine:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__cars = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def insert_car(self, *cars):
        self.__cars.extend(cars)
