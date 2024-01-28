class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return f"Pizza: size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon}"

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)

class PizzaDirector:
    def make_pizza(self, builder, size):
        return builder.set_size(size) \
            .add_cheese() \
            .add_pepperoni() \
            .add_mushrooms() \
            .add_onions() \
            .add_bacon() \
            .build()


if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector()

    pizza = director.make_pizza(builder, size="Large")
    print(pizza)
