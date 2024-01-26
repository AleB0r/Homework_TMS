class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year


car = Car("red", "Lotus", 2020)

print(car.color)
print(car.type)
print(car.year)

car.start_engine()
car.stop_engine()

car.set_color("blue")
car.set_type("BMW")
car.set_year(2022)

print(car.color)
print(car.type)
print(car.year)
