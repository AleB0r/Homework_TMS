class Item:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Name: {self.name}, Store: {self.store}, Price: {self.price} rub."


class Warehouse:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        self.__items.append(item)

    def __getitem__(self, index_or_name):
        if isinstance(index_or_name, int):
            if 0 <= index_or_name < len(self.__items):
                return self.__items[index_or_name]
        elif isinstance(index_or_name, str):
            items_with_name = []
            for item in self.__items:
                if item.name == index_or_name:
                    items_with_name.append(item)
            return items_with_name
        return None

    def sort(self, key=None, reverse=False):
        self.__items.sort(key=key, reverse=reverse)

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total_price = sum(item.price for item in self.__items) + sum(item.price for item in other.__items)
            return total_price
        else:
            raise TypeError("Unsupported operand type: Only Warehouse objects can be added.")


if __name__ == "__main__":
    item1 = Item("TV", "Store2", 50000)
    item2 = Item("Fridge", "Store1", 30000)
    item3 = Item("Phone", "Store3", 20000)
    item4 = Item("TV", "Store1", 10000)

    warehouse = Warehouse()

    warehouse.add_item(item1)
    warehouse.add_item(item2)
    warehouse.add_item(item3)
    warehouse.add_item(item4)

    index = 1
    item = warehouse[1]
    if item:
        print(f"Item at index {index}: {item}")
    else:
        print(f"Item with index {index} not found.")

    name = "TV"
    items = warehouse[name]
    if items:
        print(f"Items with name {name}:")
        for item in items:
            print(item)
    else:
        print(f"Items with name {name} not found.")

    warehouse.sort(key=lambda item: item.name)
    print("Items after sorting by name:")
    for item in warehouse.items:
        print(item)

    warehouse.sort(key=lambda item: item.store)
    print("Items after sorting by store:")
    for item in warehouse.items:
        print(item)

    warehouse.sort(key=lambda item: item.price)
    print("Items after sorting by price:")
    for item in warehouse.items:
        print(item)

    item1 = Item("TV", "Store2", 40000)
    item2 = Item("Fridge", "Store1", 80000)
    item3 = Item("Phone", "Store3", 90000)
    item4 = Item("TV", "Store1", 220000)

    new_warehouse = Warehouse()

    new_warehouse.add_item(item1)
    new_warehouse.add_item(item2)
    new_warehouse.add_item(item3)
    new_warehouse.add_item(item4)

    total_price = warehouse + new_warehouse
    print(f"Total price of items in the warehouses: {total_price} rub.")