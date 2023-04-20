from Car import Car


class Manufacturer:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def insert_car(self, car_name):
        car = Car(car_name)
        self.cars.append(car)
        return car

    def list_cars(self):
        print("Manufacturer: ", self.name)
        for car in self.cars:
            print("Cars: ", car.brand)
