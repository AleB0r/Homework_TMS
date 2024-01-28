class Item:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Название: {self.__name}, Магазин: {self.__store}, Цена: {self.__price} руб."


class Warehouse:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def get_item_by_index(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        return None

    def get_items_by_name(self, name):
        return [item for item in self.__items if item.get_name() == name]

    def sort_items_by_name(self):
        self.__items.sort(key=lambda item: item.get_name())

    def sort_items_by_store(self):
        self.__items.sort(key=lambda item: item.get_store())

    def sort_items_by_price(self):
        self.__items.sort(key=lambda item: item.get_price())

    def get_items(self):
        return self.__items

    def __add__(self, other):
        total_price = sum(item.get_price() for item in self.__items) + sum(item.get_price() for item in other.__items)
        return total_price


if __name__ == "__main__":
    item1 = Item("Телевизор", "Магазин2", 50000)
    item2 = Item("Холодильник", "Магазин1", 30000)
    item3 = Item("Смартфон", "Магазин3", 20000)
    item4 = Item("Телевизор", "Магазин1", 10000)

    warehouse = Warehouse()

    warehouse.add_item(item1)
    warehouse.add_item(item2)
    warehouse.add_item(item3)
    warehouse.add_item(item4)

    index = 1
    item = warehouse.get_item_by_index(1)
    if item:
        print(f"Товар под индексом {index}: {item}")
    else:
        print(f"Товар с индексом {index} не найден.")

    name = "Телевизор"
    items = warehouse.get_items_by_name(name)
    if items:
        print(f"Товары с названием {name}:")
        for item in items:
            print(item)
    else:
        print(f"Товары с названием {name} не найдены.")

    warehouse.sort_items_by_name()
    print("Товары после сортировки по названию:")
    for item in warehouse.get_items():
        print(item)

    warehouse.sort_items_by_store()
    print("Товары после сортировки по магазину:")
    for item in warehouse.get_items():
        print(item)

    warehouse.sort_items_by_price()
    print("Товары после сортировки по цене:")
    for item in warehouse.get_items():
        print(item)

    item1 = Item("Телевизор", "Магазин2", 40000)
    item2 = Item("Холодильник", "Магазин1", 80000)
    item3 = Item("Смартфон", "Магазин3", 90000)
    item4 = Item("Телевизор", "Магазин1", 220000)

    new_warehouse = Warehouse()

    new_warehouse.add_item(item1)
    new_warehouse.add_item(item2)
    new_warehouse.add_item(item3)
    new_warehouse.add_item(item4)

    total_price = warehouse + new_warehouse
    print(f"Общая стоимость товаров на складах: {total_price} руб.")
