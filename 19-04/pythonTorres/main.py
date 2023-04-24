from Manufacturer import Manufacturer
from Engine import Engine

land_rover = Manufacturer("Land Rover")
engine = Engine('2.0', 500.00)

evoque = land_rover.insert_car("Evoque", engine.name)
valar = land_rover.insert_car("Velar", engine.name)

land_rover.list_cars()
