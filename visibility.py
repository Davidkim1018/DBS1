class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__item = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__item.append(product)
            print("new item added")

        else:
            raise ValueError("Invalid Item")

    def get_number_of_item(self):
        return len(self.__item)

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_item())
print(type(Product()))
print(Product())
my = Product()
print(type(my) == my)
