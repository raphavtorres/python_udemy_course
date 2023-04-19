# Composition --> if the "father" is deleted the others that depend on it are as well

class Client:
    def __init__(self, name):
        self.name = name
        self.adresses = []

    def insert_address(self, street, number):
        self.adresses.append(Address(street, number))  # Object Address created with the Client

    def list_adresses(self):
        for address in self.adresses:
            print(address.street, address.number)

    def __del__(self):
        print("Deleting:", self.name)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):  # activates when garbage collector starts
        print("Deleting:", self.street, self.number)


client_1 = Client("Raphael")
client_1.insert_address('Av Brazil', 54)
client_1.insert_address('Rua B', 109)
client_1.list_adresses()

del client_1  # garbage collector is called

print("---Finish code---")
