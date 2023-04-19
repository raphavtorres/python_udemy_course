# Relation between classes:
# Association [ aggregation [ composition [] ] ]

# ASSOCIATION - Week relation
# Association --> "this object knows that the other exists"; a writer uses a tool
class Writer:
    def __init__(self, name) -> None:
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WriteTool:
    def __init__(self, name) -> None:
        self.name = name

    def write(self):
        return f'{self.name} is writing...'


writer = Writer('Raphael')
pen = WriteTool('Bic pen')
typewriter = WriteTool('typewriter')
writer.tool = pen
writer.tool = typewriter

print(pen.write())
print(writer.tool.write())





############################################################




# Aggregation --> "this object need the other to do a specific action"; a shop cart has a product
# Usually relation (1, n)
class ShoppingCart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])

    def insert_products(self, *products):
        # for product in products:
        #     self._products.append(product)
        self._products.extend(products)
        # self._products += products

    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = ShoppingCart()
p1, p2 = Product('Pen', 1.20), Product('Shirt', 20)
cart.insert_products(p1, p2)
cart.list_products()
print(cart.total())




############################################################




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
