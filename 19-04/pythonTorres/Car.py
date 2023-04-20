class Car:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand
        
