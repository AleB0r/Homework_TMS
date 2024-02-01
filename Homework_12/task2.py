class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "grass":
            self.elephant = min(self.elephant + value, 100)
            self.bee = max(self.bee - value, 0)
        elif meal == "nectar":
            self.elephant = max(self.elephant - value, 0)
            self.bee = min(self.bee + value, 100)


if __name__ == "__main__":
    BeeElephant = BeeElephant(30, 70)
    print(BeeElephant.fly())
    print(BeeElephant.trumpet())

    BeeElephant.eat("nectar", 20)
    print(BeeElephant.bee, BeeElephant.elephant)

    BeeElephant.eat("grass", 90)
    print(BeeElephant.bee, BeeElephant.elephant)
