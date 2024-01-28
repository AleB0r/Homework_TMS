class BeeElephant:
    def __init__(self, Bee, Elephant):
        self.Bee = Bee
        self.Elephant = Elephant

    def fly(self):
        return self.Bee >= self.Elephant

    def trumpet(self):
        if self.Elephant >= self.Bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "grass":
            self.Elephant = min(self.Elephant + value, 100)
            self.Bee = max(self.Bee - value, 0)
        elif meal == "nectar":
            self.Elephant = max(self.Elephant - value, 0)
            self.Bee = min(self.Bee + value, 100)


if __name__ == "__main__":
    BeeElephant = BeeElephant(30, 70)
    print(BeeElephant.fly())
    print(BeeElephant.trumpet())

    BeeElephant.eat("nectar", 20)
    print(BeeElephant.Bee, BeeElephant.Elephant)

    BeeElephant.eat("grass", 90)
    print(BeeElephant.Bee, BeeElephant.Elephant)
