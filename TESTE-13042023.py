# Problems with mutable parameters in python functions

print('-----WRONG WAY-----')
def add_customer_wrong(name='raphael', list=[]):
    list.append(name)
    return list


customer1 = add_customer_wrong('raphael')
add_customer_wrong('maristella', customer1)
print(customer1)

customer2 = add_customer_wrong('luiz')
add_customer_wrong('julia', customer2)
print(customer2)


print('\n-----RIGHT WAY-----')
def add_customer_right(name='raphael', list=None):
    if list is None:
        list = []
    list.append(name)
    return list


customer1 = add_customer_right('raphael')
add_customer_right('maristella', customer1)
print(customer1)

customer2 = add_customer_right('luiz')
add_customer_right('julia', customer2)
print(customer2)

